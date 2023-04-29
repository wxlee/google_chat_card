import requests
import json


def test_card_webhook():
    url = 'https://<YOUR_CLOUD_FUNCTION_URL>'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'card_type': 'basic',
        'title': 'Basic Card',
        'subtitle': 'This is a basic card.',
        'formatted_text': 'Hello, World!',
        'image_url': 'https://www.example.com/image.png',
        'image_alt_text': 'Example Image'
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    assert response.status_code == 200
    response_json = response.json()
    assert 'cards' in response_json
    assert len(response_json['cards']) == 1
    assert 'header' in response_json['cards'][0]
    assert 'title' in response_json['cards'][0]['header']
    assert response_json['cards'][0]['header']['title'] == 'Basic Card'
