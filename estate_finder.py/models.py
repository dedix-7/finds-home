from estate_finder import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"[({self.username}), ({self.email}), ({self.password})]"


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"{self.name}"


class PropertyType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"{self.name}"


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_type_id = db.Column(
        db.Integer, db.ForeignKey('property_type.id'), nullable=False)
    location_id = db.Column(
        db.Integer, db.ForeignKey('location.id'), nullable=False)
    status = db.Column(db.String(12), nullable=False)  # sell or rent
    size_sqft = db.Column(db.Integer)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    property_img = db.Column(
        db.String(255), nullable=False, default="default.jpg")
    property_type = db.relationship(
        'PropertyType', backref=db.backref('properties', lazy=True))
    location = db.relationship(
        'Location', backref=db.backref('properties', lazy=True))

    def __repr__(self):
        return (
            f"'{self.status}', "
            f"'{self.size_sqft}', "
            f"'{self.bedrooms}', "
            f"'{self.bathrooms}', "
            f"'{self.price}', "
            f"'{self.property_img}', "
            f"'{self.property_type}', "
            f"'{self.location}', "
            f"'{self.id}'"
        )


class PropertAgent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    contact_info = db.Column(db.String(255), nullable=False)
    agent_img = db.Column(
        db.String(255), nullable=False, default="default.jpg")

    def __repr__(self):
        return f"('{self.id}', '{self.name}', '{self.contact_info}', '{self.agent_img}')"


class Testimonials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(255), nullable=True)
    testimonial_text = db.Column(db.Text)
    client_img = db.Column(
        db.String(255), nullable=False, default="default.jpg")
    property_id = db.Column(
        db.Integer, db.ForeignKey('property.id'), nullable=False)
    property = db.relationship(
        'Property', backref=db.backref('testimonials', lazy=True))

    def __repr__(self):
        return f"( '{self.id}', '{self.client_name}', '{self.testimonial_text}', '{self.property}', '{self.client_img}')"
