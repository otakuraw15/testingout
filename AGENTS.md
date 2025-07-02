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
    python app.py
    ```
    Or, for development mode (which enables auto-reloading on code changes):
    ```bash
    flask run --debug
    ```
    (Ensure `FLASK_APP=app.py` is set in your environment, or use `python -m flask run --debug`)


4.  **Open your web browser** and go to:
    `http://127.0.0.1:5000/` (or the address shown in your terminal, typically port 5000).

### How to Use:

1.  The application will attempt to get your geolocation when you submit the form. Your browser will likely ask for permission to access your location. You must **allow location access** for the app to work correctly.
2.  Fill in the three data fields: "Field 1", "Field 2", and "Field 3".
3.  Click the "Get Location & Send Data" button.
4.  Your current latitude and longitude will be displayed.
5.  The form data and your location will be sent to the backend.
6.  A message will appear indicating whether the data submission was successful or if an error occurred.
7.  Submitted data (including geolocation) will be logged to the console where the Flask `app.py` is running.

### Notes for Agent:

*   The application currently only logs the received data on the server-side console. No database or persistent storage is implemented.
*   Error handling for geolocation (e.g., permission denied, location unavailable) is implemented on the client-side.
*   The backend expects JSON data at the `/submit_data` endpoint.
*   Ensure Flask is installed in the environment before running.
*   The `templates` and `static` folders must be in the same directory as `app.py` for Flask to find the HTML, CSS, and JS files correctly.
