from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from io import BytesIO

app = Flask(__name__)
CORS(app)

# Mock database to track events (in-memory for testing purposes)
mock_database = []

# Counter to track the number of users
user_counter = 0

@app.route('/')
def home():
    return "Welcome to the Tracking Pixel Service!"

@app.route('/tracking-pixel', methods=['GET'])
def tracking_pixel():
    global user_counter
    # Increment the user counter
    user_counter += 1

    # Extract query parameters
    user_id = request.args.get('user_id')
    event = request.args.get('event')

    # Log the event if both user_id and event are provided
    log_message = ""
    if user_id and event:
        mock_database.append({"user_id": user_id, "event": event})
        log_message = f"Tracking Pixel logged: User ID = {user_id}, Event = {event}"
        print(log_message)
        return jsonify(message=log_message, user_count=user_counter)

    # Return a 1x1 transparent pixel if no user_id or event is provided
    pixel = BytesIO()
    pixel.write(b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b')
    pixel.seek(0)
    return send_file(pixel, mimetype='image/gif')

if __name__ == '__main__':
    app.run(debug=True)
    