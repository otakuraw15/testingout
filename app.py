from flask import Flask, request, jsonify, render_template
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_data', methods=['POST'])
def submit_data():
    if request.is_json:
        data = request.get_json()
        app.logger.info(f"Received data: {data}") # Log to console

        # You would typically process or store this data here
        # For example, save to a database, etc.

        return jsonify({"message": "Data received successfully!", "data": data}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
