''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

# import flask app module
from flask import Flask, render_template, request
# import emotion_detector function
from EmotionDetection.emotion_detection import emotion_detector

# initial flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''
    detect the emotion of the text sent to emotionDetection router

    args:
        text to analyze
    return:
        analyzed result
    '''
    # get text to detect from request body
    text_to_detect = request.args.get('textToAnalyze')

    # pass the response to emotion_detector function and store the result
    response = emotion_detector(text_to_detect)
    text = f"For the given statement, the system response is: <br>"
    for key, value in response.items():
        text += f"{key} : {value} <br>"
        
    return text

@app.route("/")
def render_index_page():
    '''
    render the html page

    args:

    return:
        rendered html page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    '''
    run server
    '''
    app.run(host="0.0.0.0", port=5000)
