

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

