import json
# from Card import *
from card_utils import *
from flask import Flask, request, jsonify

app = Flask(__name__)

# @app.route('/card', methods=['POST'])
# def card_webhook():
#     req = request.get_json()
#     card_type = req.get('card_type')
#     if card_type == 'basic':
#         title = req.get('title')
#         subtitle = req.get('subtitle')
#         formatted_text = req.get('formatted_text')
#         image_url = req.get('image_url')
#         image_alt_text = req.get('image_alt_text')
#         card_json = create_basic_card(title, subtitle, formatted_text, image_url, image_alt_text)
#     elif card_type == 'button':
#         title = req.get('title')
#         subtitle = req.get('subtitle')
#         formatted_text = req.get('formatted_text')
#         image_url = req.get('image_url')
#         image_alt_text = req.get('image_alt_text')
#         button_text = req.get('button_text')
#         button_url = req.get('button_url')
#         card_json = create_button_card(title, subtitle, formatted_text, image_url, image_alt_text, button_text, button_url)
#     elif card_type == 'confirmation':
#         title = req.get('title')
#         subtitle = req.get('subtitle')
#         formatted_text = req.get('formatted_text')
#         image_url = req.get('image_url')
#         image_alt_text = req.get('image_alt_text')
#         confirm_button_text = req.get('confirm_button_text')
#         deny_button_text = req.get('deny_button_text')
#         card_json = create_confirmation_card(title, subtitle, formatted_text, image_url, image_alt_text, confirm_button_text, deny_button_text)
#     elif card_type == 'chart':
#         title = req.get('title')
#         subtitle = req.get('subtitle')
#         chart_data = req.get('chart_data')
#         card_json = create_chart_card(title, subtitle, chart_data)
#     elif card_type == 'list':
#         title = req.get('title')
#         subtitle = req.get('subtitle')
#         items = req.get('items')
#         card_json = create_list_card(title, subtitle, items)
#     else:
#         card_json = {}

#     return jsonify(card_json)

# Handle basic card request
@app.route('/card/basic', methods=['POST'])
def basic_card():
    data = request.get_json()
    card = create_basic_card(data)
    return jsonify(card)

# Handle button card request
@app.route('/card/button', methods=['POST'])
def button_card():
    data = request.get_json()
    card = create_button_card(data)
    return jsonify(card)

# Handle confirmation card request
@app.route('/card/confirmation', methods=['POST'])
def confirmation_card():
    data = request.get_json()
    card = create_confirmation_card(data)
    return jsonify(card)

# Handle chart card request
@app.route('/card/chart', methods=['POST'])
def chart_card():
    data = request.get_json()
    card = create_chart_card(data)
    return jsonify(card)

# Handle list card request
@app.route('/card/list', methods=['POST'])
def list_card():
    data = request.get_json()
    card = create_list_card(data)
    return jsonify(card)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)