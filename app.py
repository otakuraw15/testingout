from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import logging
import os
from datetime import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database Configuration
# Prioritize environment variables for security and flexibility
DB_USER = os.environ.get('DB_USER', 'your_mysql_user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'your_mysql_password')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'geolocation_db')

# SQLAlchemy URI for MySQL using PyMySQL
# mysql+pymysql://<username>:<password>@<host>/<dbname>
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the database model
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    field1 = db.Column(db.String(255), nullable=False)
    field2 = db.Column(db.String(255), nullable=False)
    field3 = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Submission id={self.id} lat={self.latitude} lon={self.longitude}>"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_data', methods=['POST'])
def submit_data():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    app.logger.info(f"Received data: {data}")

    required_fields = ['latitude', 'longitude', 'field1', 'field2', 'field3']
    if not all(field in data for field in required_fields):
        missing = [field for field in required_fields if field not in data]
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    try:
        new_submission = Submission(
            latitude=float(data['latitude']),
            longitude=float(data['longitude']),
            field1=str(data['field1']),
            field2=str(data['field2']),
            field3=str(data['field3'])
        )
        db.session.add(new_submission)
        db.session.commit()
        app.logger.info(f"Data saved to database: {new_submission}")
        return jsonify({
            "message": "Data received and saved successfully!",
            "submission_id": new_submission.id
        }), 201
    except ValueError as ve:
        app.logger.error(f"Invalid data format: {ve}")
        return jsonify({"error": "Invalid data format. Latitude and longitude must be numbers."}), 400
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Database error: {e}")
        # It's good practice to not expose raw exception details to the client in production
        return jsonify({"error": "Could not save data to database. Check server logs."}), 500

# It's good practice to create tables using a Flask CLI command or a migration tool
# For simplicity in this example, you can create tables from the Python shell:
# from app import app, db
# with app.app_context():
#     db.create_all()
#
# Or add a CLI command:
# @app.cli.command("init-db")
# def init_db_command():
#     """Creates the database tables."""
#     db.create_all()
#     print("Initialized the database.")

if __name__ == '__main__':
    # Make sure to create the database 'geolocation_db' in MySQL first,
    # and grant appropriate permissions to 'your_mysql_user'.
    # Then run the db.create_all() command as mentioned above.
    app.run(debug=True, port=5000)
