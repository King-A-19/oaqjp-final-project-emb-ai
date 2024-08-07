# Import Flask, render_template, request from the flask framework package
from flask import Flask, request, jsonify, render_template

# Import the emotion_detector function from the EmotionDetection module
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def analyze_emotion():
    # Retrieve the text to analyze from the query parameters
    text_to_analyse = request.args.get('textToAnalyze')

    # Call the emotion_detector function to analyze the text
    response = emotion_detector(text_to_analyse)

    # Prepare the response in the specified format
    return (f"For the given statement, the system response is "
            f"'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, "
            f"'joy': {response['joy']}, and "
            f"'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)
