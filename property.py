"""
This script is responsible for setting up initial data in the estate_finder
application's database. It imports the necessary modules and Flask
app instance,as well as the SQLAlchemy database instance and the
models for `Location`, `PropertyType`, and `Property`.

The script then enters the application context using `with app.app_context():`
to ensure that the database operations are performed within the correct
context. This is a necessary step when using Flask's application
context to interact with the database.

Within the context, the script creates instances of `Location`, `PropertyType`
models, representing two different cities and two types of properties.
These instances are added to the database session and committed, which
saves them to the database.

Next, the script creates instances of `Property`, linking each property to a
`Location` and a `PropertyType`.These properties represent real estate listings
with details such as image file names,status (for sale or for rent),size,number
of bedrooms and bathrooms, and price.The properties are also added to database
session and committed.

Finally, the script prints a confirmation message indicating that the data has
been added successfully. This output can be useful for verifying the script
has run without errors and that the initial data has been populated expected.
"""


# importing necessary modules,  creating the Flask app and SQLAlchemy instance
from estate_finder import app, db
from estate_finder.models import Location, PropertyType, Property

# Use the app's context to interact with the database
with app.app_context():
    # Create some instances of Location and PropertyType if not already present
    location1 = Location(name='City A')
    location2 = Location(name='City B')

    property_type1 = PropertyType(name='House')
    property_type2 = PropertyType(name='Apartment')

    # Add the instances to the session
    db.session.add_all([location1, location2, property_type1, property_type2])

    # Commit the changes to the database
    db.session.commit()

    # Create instances of Property and link them to Location and PropertyType
    property1 = Property(
        image_file='property1.jpg',
        property_type=property_type1,
        location=location1,
        status='For Sale',
        size_sqft=2000,
        bedrooms=3,
        bathrooms=2,
        price=500000.0
    )

    property2 = Property(
        image_file='property2.jpg',
        property_type=property_type2,
        location=location2,
        status='For Rent',
        size_sqft=1500,
        bedrooms=2,
        bathrooms=1,
        price=1200.0
    )

    # Add the instances to the session
    db.session.add_all([property1, property2])

    # Commit the changes to the database
    db.session.commit()

    print("Data added successfully.")
