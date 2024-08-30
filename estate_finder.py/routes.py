from flask import (
    render_template,
    url_for,
    redirect,
    flash,
    jsonify,
    request, send_from_directory
)
from werkzeug.utils import secure_filename
import os
from estate_finder import app, db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required
from estate_finder.models import (
    Location, Property,
    PropertyType, User,
    PropertAgent, Testimonials
)
from estate_finder.form import PropertyForm, LoginForm, RegistrationForm
from collections import defaultdict
from sqlalchemy import func

@app.route('/')
@app.route('/home')
def home():
    locations = Location.query.all()
    prop_type = PropertyType.query.all()
    agents = PropertAgent.query.all()
    page = request.args.get('page', 1, type=int)
    per_page = 6
    properties = Property.query.order_by(Property.id.desc()).\
        paginate(page=page, per_page=per_page)

    properties_2 = Property.query.all()
    count = defaultdict(int)
    for prop in properties_2:
        count[prop.property_type.name] += 1

    return render_template('home.html',
                           locations=locations,
                           prop_type=prop_type,
                           properties=properties,
                           agents=agents,
                           count=count)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/property-list')
def property_list():
    locations = Location.query.all()
    prop_type = PropertyType.query.all()
    page = request.args.get('page', 1, type=int)
    per_page = 6
    properties = Property.query.order_by(Property.id.desc()).\
        paginate(page=page, per_page=per_page)
    return render_template('property-list.html',
                           properties=properties,
                           locations=locations,
                           props=prop_type)


@app.route('/property-type')
def property_type():
    prop_type = PropertyType.query.all()
    properties = Property.query.all()
    count = defaultdict(int)
    for prop in properties:
        count[prop.property_type.name] += 1
    locations = Location.query.all()
    return render_template('property-type.html',
                           locations=locations,
                           props=prop_type,
                           count=count)


@app.route('/property-agent')
def property_agent():
    agents = PropertAgent.query.all()
    return render_template('property-agent.html', agents=agents)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = (bcrypt.generate_password_hash
                           (form.password.data)
                           .decode('utf-8'))
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('add_property'))
        else:
            flash(
                'Login Unsuccessful, Please check email and password',
                "danger")
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/add_property', methods=['GET', 'POST'])
@login_required
def add_property():
    form = PropertyForm()
    if form.validate_on_submit():
        # Fetch the PropertyType instance based on the selected type name
        property_type = PropertyType.query.filter_by(
            name=form.property_type.data).first()
        location = Location.query.filter_by(
            name=form.propertyLocation.data).first()
        if property_type and location:
            if form.propertyImage.data:
                # Save the image file
                image = form.propertyImage.data
                filename = secure_filename(image.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                try:
                    image.save(file_path)
                except Exception as e:
                    flash(f"Error saving file: {str(e)}", "danger")
                    return redirect(url_for('add_property'))

            else:
                filename = None

            prop = Property(
                property_type=property_type,
                status=form.propertyStatus.data,
                location=location,
                size_sqft=form.propertySize.data,
                bedrooms=form.propertyBedrooms.data,
                bathrooms=form.propertyBathrooms.data,
                price=form.propertyPrice.data,
                property_img=filename
                # Save the image filename in the database
            )
            db.session.add(prop)
            db.session.commit()
            flash("Property added successfully", "success")
            return redirect(url_for('property_list'))
        else:
            flash("Invalid Property Type or Location", "danger")
    return render_template('add_property.html', form=form)


@app.route('/uploads/<filename>')
def serve_uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/testimonial')
def testimonial():
    quotes = Testimonials.query.all()
    return render_template('testimonial.html', quotes=quotes)


@app.route('/404')
def not_found():
    return render_template('404.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


from sqlalchemy.orm import joinedload


@app.route('/properties_by_type/<property_type_name>')
def properties_by_type(property_type_name):
    # Query properties based on the property type's name using a join
    properties = Property.query.join(Property.property_type).\
        filter(PropertyType.name == property_type_name).\
        options(joinedload(Property.property_type)).all()
    if not properties:
        return redirect(url_for('not_found'))
    return render_template('properties_by_type.html', properties=properties)


@app.route('/filter-by-status/<status>')
def filter_by_status(status):
    print(f"Filtering properties by status: {status}")
    # Add this print statement

    # Query properties based on provided status (case-insensitive)
    properties = Property.query.filter(func.lower(
        Property.status) == func.lower(status)).all()

    print(f"Found {len(properties)} properties")  # Add this print statement

# You may want to handle the case when no properties are found for given status

    locations = Location.query.all()
    prop_type = PropertyType.query.all()

    return render_template('property_list_status.html',
                           properties=properties,
                           locations=locations,
                           props=prop_type)


@app.route('/property-details/<int:property_id>')
def property_details(property_id):
    # Fetch the property based on the property_id
    property = Property.query.get(property_id)

    if property:
        return render_template('property_details.html', property=property)
    else:
        # Handle the case when the property is not found
        return render_template('404.html')
