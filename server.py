"""
This module sets up a Flask application to perform emotion detection
using the EmotionDetection library.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)
@app.route("/emotionDetector")

def sent_analyzer():
    """
    Analyze the given text for emotions.

    Retrieves the text from the query parameters, uses the emotion_detector
    function to analyze it, and returns the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return f"For the given statement, the system response is {result}"

@app.route("/")

def render_index_page():
    """
    Render the index page of the application.

    Serves the 'index.html' template as the home page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    