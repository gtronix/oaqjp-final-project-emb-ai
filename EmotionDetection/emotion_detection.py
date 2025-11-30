import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    myobj = { "raw_document": { "text": text_to_analyse } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    
    formatted_response = json.loads(response.text)
    
    # emotions = ('anger', 'disgust', 'fear', 'joy', 'sadness')

    anger_score = formatted_response['emotionPredictions'][0]['emotion'].get('anger', 0)
    disgust_score = formatted_response['emotionPredictions'][0]['emotion'].get('disgust', 0)
    fear_score = formatted_response['emotionPredictions'][0]['emotion'].get('fear', 0)
    joy_score = formatted_response['emotionPredictions'][0]['emotion'].get('joy', 0)
    sadness_score = formatted_response['emotionPredictions'][0]['emotion'].get('sadness', 0)
    
    # Create emotions dictionary
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
