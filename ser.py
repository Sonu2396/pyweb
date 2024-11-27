from flask import Flask, jsonify
import base64
import os

#GOOGLE_API_KEY = os.environ["AIzaSyC2XBKaOmaMQZFK43pvy9q13fQ-8YKi2FI"]

GOOGLE_API_KEY = "AIzaSyC2XBKaOmaMQZFK43pvy9q13fQ-8YKi2FI"


import google.generativeai as genai

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
def hello_worldold():
  # Simple logic to return a message
  message = "Hello, world old!"

  # Return JSON response
  return jsonify({'message': message})

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json
    text = data['text']
    base64_string = data['base64_string']

    # Decode the base64 string
    decoded_bytes = base64.b64decode(base64_string)
    decoded_text = decoded_bytes.decode('utf-8')

    # Process the text and decoded text as needed
    # ... your processing logic here ...

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content("Write me a poem")
    #print(response.text)

  
    return jsonify({'message': 'Response : ' + response.text})

@app.route('/process_data_get', methods=['GET'])
def process_data_get():
   
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content("Write me a poem")
    #print(response.text)
    return jsonify({'message': 'Response : ' + response.text})

if __name__ == '__main__':
  # Configure for Render deployment (optional)
  # app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
  app.run(debug=True)
