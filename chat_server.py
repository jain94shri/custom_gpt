from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
app = Flask(__name__)

# Load the API key from an environment variable for security
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('chat_interface.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['input']
    try:
        # Correctly use the new API method
        response = openai.Completion.create(
            model="g-HfdvT3XCz-spandan-2",
            prompt="Translate the following English text to French: 'Hello, how are you?'",
            max_tokens=60
        )
        # Assuming the API response structure aligns with the following line
        return jsonify({'response': response['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
