import json

def create_basic_card(data):
    """Create a basic card."""
    title = data['title']
    subtitle = data['subtitle']
    text = data['text']
    image_url = data['image_url']
    alt_text = data['alt_text']

    card = {
        "cards": [
            {
                "header": {
                    "title": title,
                    "subtitle": subtitle,
                    "imageStyle": "IMAGE"
                },
                "sections": [
                    {
                        "widgets": [
                            {
                                "image": {
                                    "imageUrl": image_url,
                                    "altText": alt_text
                                }
                            },
                            {
                                "textParagraph": {
                                    "text": text
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }

    return json.dumps(card)

def create_button_card(data):
    """Create a button card."""
    title = data['title']
    subtitle = data['subtitle']
    text = data['text']
    button_text = data['button_text']
    button_url = data['button_url']

    card = {
        "cards": [
            {
                "header": {
                    "title": title,
                    "subtitle": subtitle,
                    "imageStyle": "IMAGE"
                },
                "sections": [
                    {
                        "widgets": [
                            {
                                "textParagraph": {
                                    "text": text
                                }
                            },
                            {
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
                ]
            }
        ]
    }

    return json.dumps(card)

def create_confirmation_card(data):
    """Create a confirmation card."""
    title = data['title']
    subtitle = data['subtitle']
    text = data['text']

    card = {
        "cards": [
            {
                "header": {
                    "title": title,
                    "subtitle": subtitle,
                    "imageStyle": "IMAGE"
                },
                "sections": [
                    {
                        "widgets": [
                            {
                                "textParagraph": {
                                    "text": text
                                }
                            }
                        ]
                    },
                    {
                        "widgets": [
                            {
                                "buttons": [
                                    {
                                        "textButton": {
                                            "text": "Yes",
                                            "onClick": {
                                                "action": {
                                                    "actionMethodName": "confirmation",
                                                    "parameters": [
                                                        {
                                                            "key": "confirm",
                                                            "value": "true"
                                                        }
                                                    ]
                                                }
                                            }
                                        }
                                    },
                                    {
                                        "textButton": {
                                            "text": "No",
                                            "onClick": {
                                                "action": {
                                                    "actionMethodName": "confirmation",
                                                    "parameters": [
                                                        {
                                                            "key": "confirm",
                                                            "value": "false"
                                                        }
                                                    ]
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

    return json.dumps(card)

def create_chart_card(data):
    """Create a chart card."""
    title = data['title']
    subtitle = data['subtitle']
    chart_type = data['chart_type']
    data_points = data['data_points']

    chart_data = []
    for label, value in data_points.items():
        chart_data.append({
            "label": label,
            "value":
        value
    })

    card = {
        "cards": [
            {
                "header": {
                    "title": title,
                    "subtitle": subtitle,
                    "imageStyle": "IMAGE"
                },
                "sections": [
                    {
                        "widgets": [
                            {
                                "chart": {
                                    "spec": {
                                        "title": title,
                                        "chartData": {
                                            "dataSets": [
                                                {
                                                    "label": "",
                                                    "data": chart_data,
                                                    "dataType": chart_type
                                                }
                                            ]
                                        },
                                        "legend": "RIGHT_LEGEND",
                                        "chartType": chart_type,
                                        "maxValue": max(data_points.values()),
                                        "minValue": 0,
                                        "header": {
                                            "data": [
                                                {
                                                    "type": "CATEGORY",
                                                    "label": "Label"
                                                },
                                                {
                                                    "type": "NUMBER",
                                                    "label": "Value"
                                                }
                                            ]
                                        }
                                    }
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }

    return json.dumps(card)

def create_list_card(data):
    """Create a list card."""
    title = data['title']
    subtitle = data['subtitle']
    items = data['items']
    item_list = []
    for item in items:
        item_list.append({
            "info": {
                "title": item['text']
            },
            "image": {
                "imageUrl": item['image_url'],
                "altText": item['image_alt_text']
            }
        })

    card = {
        "cards": [
            {
                "header": {
                    "title": title,
                    "subtitle": subtitle,
                    "imageStyle": "IMAGE"
                },
                "sections": [
                    {
                        "widgets": [
                            {
                                "list": {
                                    "items": item_list
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }

    return json.dumps(card)
