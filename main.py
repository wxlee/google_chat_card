import json

from flask import Flask, request, jsonify


def create_basic_card(title, subtitle, formatted_text, image_url, image_alt_text):
    basic_card = {
        "cards": [
            {
                "sections": [
                    {
                        "widgets": [
                            {
                                "image": {
                                    "imageUrl": image_url,
                                    "accessibilityText": image_alt_text
                                }
                            },
                            {
                                "textParagraph": {
                                    "text": formatted_text
                                }
                            }
                        ]
                    }
                ],
                "header": {
                    "title": title,
                    "subtitle": subtitle
                }
            }
        ]
    }
    return basic_card


def create_button_card(title, subtitle, formatted_text, image_url, image_alt_text, button_text, button_url):
    button_card = {
        "cards": [
            {
                "sections": [
                    {
                        "widgets": [
                            {
                                "image": {
                                    "imageUrl": image_url,
                                    "accessibilityText": image_alt_text
                                }
                            },
                            {
                                "textParagraph": {
                                    "text": formatted_text
                                }
                            }
                        ]
                    }
                ],
                "header": {
                    "title": title,
                    "subtitle": subtitle
                },
                "buttons": [
                    {
                        "textButton": {
                            "text": button_text,
                            "onClick": {
                                "openLink": {
                                    "url": button_url
                                }
                            }
                        }
                    }
                ]
            }
        ]
    }
    return button_card


def create_confirmation_card(title, subtitle, formatted_text, image_url, image_alt_text, confirm_button_text, deny_button_text):
    confirmation_card = {
        "cards": [
            {
                "sections": [
                    {
                        "widgets": [
                            {
                                "image": {
                                    "imageUrl": image_url,
                                    "accessibilityText": image_alt_text
                                }
                            },
                            {
                                "textParagraph": {
                                    "text": formatted_text
                                }
                            }
                        ]
                    }
                ],
                "header": {
                    "title": title,
                    "subtitle": subtitle
                },
                "buttons": [
                    {
                        "textButton": {
                            "text": confirm_button_text,
                            "onClick": {
                                "action": {
                                    "actionMethodName": "confirm"
                                }
                            }
                        }
                    },
                    {
                        "textButton": {
                            "text": deny_button_text,
                            "onClick": {
                                "action": {
                                    "actionMethodName": "deny"
                                }
                            }
                        }
                    }
                ]
            }
        ]
    }
    return confirmation_card


def create_chart_card(title, subtitle, chart_data):
    chart_card = {
        "cards": [
            {
                "header": {
                    "title": title,
                    "subtitle": subtitle
                },
                "sections": [
                    {
                        "widgets": [
                            {
                                "chart": {
                                    "spec": chart_data
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
    return chart_card


def create_list_card(title, subtitle, items):
    list_card = {
        "cards": [
            {
                "header": {
                    "title": title,
                    "subtitle": subtitle
                },
                "sections": [
                    {
                        "widgets": [
                            {
                                "list": {
                                    "items": items
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
    return list_card


app = Flask(__name__)

@app.route('/card', methods=['POST'])
def card_webhook():
    req = request.get_json()
    card_type = req.get('card_type')
    if card_type == 'basic':
        title = req.get('title')
        subtitle = req.get('subtitle')
        formatted_text = req.get('formatted_text')
        image_url = req.get('image_url')
        image_alt_text = req.get('image_alt_text')
        card_json = create_basic_card(title, subtitle, formatted_text, image_url, image_alt_text)
    elif card_type == 'button':
        title = req.get('title')
        subtitle = req.get('subtitle')
        formatted_text = req.get('formatted_text')
        image_url = req.get('image_url')
        image_alt_text = req.get('image_alt_text')
        button_text = req.get('button_text')
        button_url = req.get('button_url')
        card_json = create_button_card(title, subtitle, formatted_text, image_url, image_alt_text, button_text, button_url)
    elif card_type == 'confirmation':
        title = req.get('title')
        subtitle = req.get('subtitle')
        formatted_text = req.get('formatted_text')
        image_url = req.get('image_url')
        image_alt_text = req.get('image_alt_text')
        confirm_button_text = req.get('confirm_button_text')
        deny_button_text = req.get('deny_button_text')
        card_json = create_confirmation_card(title, subtitle, formatted_text, image_url, image_alt_text, confirm_button_text, deny_button_text)
    elif card_type == 'chart':
        title = req.get('title')
        subtitle = req.get('subtitle')
        chart_data = req.get('chart_data')
        card_json = create_chart_card(title, subtitle, chart_data)
    elif card_type == 'list':
        title = req.get('title')
        subtitle = req.get('subtitle')
        items = req.get('items')
        card_json = create_list_card(title, subtitle, items)
    else:
        card_json = {}

    return jsonify(card_json)



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)