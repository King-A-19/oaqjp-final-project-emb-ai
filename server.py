# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app 
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the info
    emotions = response_dict['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)

   
    return "For the given statement, the system response is {} The dominant emotion is  {}.".format(emotions.split('_')[1], dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)