from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello_world():
  # Simple logic to return a message
  message = "Hello, world!"

  # Return JSON response
  return jsonify({'message': message})

@app.route('/echo', methods=['POST'])
def echo():
  # Get data from request
  data = request.get_json()
  if data is None:
    return jsonify({'error': 'No data provided'}), 400

  # Get message from data
  message = data.get('message')

  # Process data (replace with your logic)
  # Here, we simply echo the message back
  echo_message = message

  # Return JSON response
  return jsonify({'echo': echo_message})






@app.route('/helloold', methods=['GET'])
def hello_world():
  # Simple logic to return a message
  message = "Hello, world!"

  # Return JSON response
  return jsonify({'message': message})

if __name__ == '__main__':
  # Configure for Render deployment (optional)
  # app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
  app.run(debug=True)
