"""
This module creates a Flask web application that detects emotions in text.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def analyze_emotion():
    """
    Analyzes the emotion of the text provided as a query parameter.
    """
    text_to_analyse = request.args.get('textToAnalyze')

    # Check if the input text is blank or None
    if not text_to_analyse:
        return 'Invalid text! Please try again.', 200

    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again.', 200

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index page of the web application.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
