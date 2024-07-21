import google.generativeai as genai
import os
import logging

# Set the API key
api_key = "AIzaSyAzCjpm-mY4WCfkZnyj5V9NladpSrs3QvQ"

# Check if API key is provided
if not api_key:
    raise ValueError("API key not found. Please set the API_KEY environment variable.")

# Configure logging
logging.basicConfig(level=logging.DEBUG)

try:
    # Configure the API key
    genai.configure(api_key=api_key)
    logging.debug("API key configured successfully.")

    # Initialize the model
    model = genai.GenerativeModel('gemini-1.5-flash')
    logging.debug("Model initialized successfully.")

    # Generate content
    response = model.generate_content("Write a story about an AI and magic")
    logging.debug("Content generated successfully.")
    print(response.text)

except Exception as e:
    logging.error(f"An error occurred: {e}")
    if hasattr(e, 'details'):
        logging.error(f"Error details: {e.details}")
