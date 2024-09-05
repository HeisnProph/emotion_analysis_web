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
    
    # # error handler
    # if response.status_code != 200:
    #     return None
    # # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Extracting sentiment label and score from the response
    # Returning a dictionary containing sentiment analysis results
    return formatted_response   