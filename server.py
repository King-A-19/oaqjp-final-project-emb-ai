from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def analyze_emotion():
    text_to_analyse = request.args.get('textToAnalyze')

    # Check if the input text is blank or None
    if not text_to_analyse:
        return 'Invalid text! Please try again.', 200

    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again.', 200

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
    app.run(host="0.0.0.0", port=5000)
