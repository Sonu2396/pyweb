from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_data():
  # Get data from request
  data = request.get_json()
  if data is None:
    return jsonify({'error': 'No data provided'}), 400

  # Get input parameters
  message = data.get('message')

  # Process data (replace with your logic)
  # Here, we simply reverse the message
  processed_message = message[::-1]

  # Return output as JSON
  return jsonify({'processed_message': processed_message})

if __name__ == '__main__':
  # Configure for Render deployment (optional)
  # app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
  app.run(debug=True)
