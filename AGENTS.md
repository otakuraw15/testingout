## Geolocation Data Sender Web App

This web application allows users to send their geolocation along with three custom data fields to a backend server.

### Project Structure:

- `app.py`: The main Flask application file. It serves the frontend and handles data submission.
- `templates/index.html`: The HTML structure for the web page.
- `static/style.css`: CSS styles for the web page.
- `static/script.js`: JavaScript code for handling geolocation, form submission, and communication with the backend.

### How to Run:

1.  **Prerequisites:**
    *   Python 3.x installed.
    *   Flask installed. If not, install it using pip:
        ```bash
        pip install Flask
        ```

2.  **Navigate to the project directory** in your terminal.

3.  **Run the Flask application:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Database Setup (MySQL):**
    *   Ensure you have a MySQL server running and accessible.
    *   Create a database for this application. For example, `CREATE DATABASE geolocation_db;`
    *   Create a MySQL user and grant it permissions to this database. For example:
        ```sql
        CREATE USER 'your_user'@'localhost' IDENTIFIED BY 'your_password';
        GRANT ALL PRIVILEGES ON geolocation_db.* TO 'your_user'@'localhost';
        FLUSH PRIVILEGES;
        ```
        Replace `'your_user'`, `'localhost'`, and `'your_password'` as appropriate.
    *   **Configure Database Connection:**
        The application expects the following environment variables to be set for the database connection:
        *   `DB_USER`: Your MySQL username (defaults to `your_mysql_user` if not set)
        *   `DB_PASSWORD`: Your MySQL password (defaults to `your_mysql_password` if not set)
        *   `DB_HOST`: The host of your MySQL server (defaults to `localhost` if not set)
        *   `DB_NAME`: The name of your database (defaults to `geolocation_db` if not set)
        You can set these in your shell before running the app:
        ```bash
        export DB_USER="your_actual_user"
        export DB_PASSWORD="your_actual_password"
        export DB_HOST="localhost" # or your DB host
        export DB_NAME="geolocation_db"
        ```
        Alternatively, for development, you can modify the default values directly in `app.py`, but using environment variables is recommended for security and flexibility.

3.  **Initialize Database Tables:**
    Once the Flask application is configured with the correct database credentials, you need to create the necessary tables. Open a Python shell in your project directory (where `app.py` is located) and run the following commands:
    ```bash
    flask shell
    ```
    Then, in the Flask shell:
    ```python
    from app import db
    db.create_all()
    exit()
    ```
    This will create the `submission` table based on the model defined in `app.py`.

4.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    Or, for development mode (which enables auto-reloading on code changes and uses the Flask CLI):
    ```bash
    flask run --debug
    ```
    (Ensure `FLASK_APP=app.py` is set in your environment if using `flask run`).

5.  **Open your web browser** and go to:
    `http://127.0.0.1:5000/` (or the address shown in your terminal, typically port 5000).

### How to Use:

1.  The application will attempt to get your geolocation when you submit the form. Your browser will likely ask for permission to access your location. You must **allow location access** for the app to work correctly.
2.  Fill in the three data fields: "Field 1", "Field 2", and "Field 3".
3.  Click the "Get Location & Send Data" button.
4.  Your current latitude and longitude will be displayed.
5.  The form data and your location will be sent to the backend and stored in the MySQL database.
6.  A message will appear indicating whether the data submission was successful or if an error occurred.
7.  Submitted data is logged to the server console and saved in the `submission` table in your MySQL database.

### Notes for Agent:

*   The application now uses a MySQL database via Flask-SQLAlchemy and PyMySQL.
*   **Database credentials and connection details should be managed securely, preferably via environment variables.** Default credentials in `app.py` are for illustrative purposes only.
*   The `submission` table schema is defined in the `Submission` class in `app.py`.
*   Ensure `db.create_all()` is run within the application context to set up tables before running the app for the first time against a new database.
*   Error handling for geolocation is on the client-side. Database errors are caught on the server-side.
*   The backend expects JSON data at the `/submit_data` endpoint.
*   The `templates` and `static` folders must be in the same directory as `app.py`.
*   A `requirements.txt` file should be created/updated with `Flask`, `Flask-SQLAlchemy`, and `PyMySQL`.
