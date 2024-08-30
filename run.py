"""
This is the entry point for the estate_finder Flask application.
It sets up the Flask app and database instance, initializes the
Flask-Migrate extension for handling database migrations, and
runs the app in debug mode if the script is executed directly.

The `app` and `db` objects are imported from the `estate_finder`
module, which is assumed to contain the Flask application instance
and the database object. The `Migrate` class from the `flask_migrate`
module is instantiated with the `app` and `db` objects to manage
database migrations.

The `if __name__ == "__main__":` check ensures that the app is only
run if the script is executed directly, and not when it is imported
as a module. When running the app in debug mode, the Flask development
server will automatically reload the app when code changes are detected,
and it will provide detailed error pages when an unhandled exception occurs.

It is important to note that debug mode should never be used in a production
environment due to security risks, as it allows the execution of arbitrary
Python code from the browser [3].

The script concludes by running the Flask application with debug mode enabled,
which is suitable for development purposes.
"""


from estate_finder import app, db
from flask_migrate import Migrate

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
