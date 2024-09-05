import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    #  error handler
    if response.status_code == 400:
        emotion_scores = {
            "anger" : None,
            "disgust" : None,
            "fear" : None,
            "joy" : None,
            "sadness" : None,
            "dominant emotion" : None
        }
        return emotion_scores
    #  Parsing the JSON response from the API
    emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant emotion'] = dominant_emotion 
    
    # Extracting sentiment label and score from the response
    # Returning a dictionary containing sentiment analysis results
    return emotion_scores