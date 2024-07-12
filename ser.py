from flask import Flask, jsonify

app = Flask(__name__)

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
