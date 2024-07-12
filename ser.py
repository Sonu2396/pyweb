from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/process', methods=['GET', 'POST'])
def hello_world():
  if request.method == 'GET':
    # Handle GET request
    message = "Hello, world! This is a GET request."
  elif request.method == 'POST':
    # Handle POST request
    data = request.get_json()
    if data is None:
      return jsonify({'error': 'No data provided'}), 400
    name = data.get('name')
    message = f"Hello, {name}! This is a POST request."
  else:
    # Handle unsupported methods
    return jsonify({'error': 'Method not allowed'}), 405

  # Return JSON response
  return jsonify({'message': message})






@app.route('/hello', methods=['GET'])
def hello_world():
  # Simple logic to return a message
  message = "Hello, world!"

  # Return JSON response
  return jsonify({'message': message})

if __name__ == '__main__':
  # Configure for Render deployment (optional)
  # app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
  app.run(debug=True)
