
## CURL test case

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "card_type": "basic",
        "title": "Basic Card",
        "subtitle": "This is a basic card.",
        "formatted_text": "Hello, World!",
        "image_url": "https://www.example.com/image.png",
        "image_alt_text": "Example Image"
      }' \
  <YOUR_CLOUD_FUNCTION_URL>
```

```bash
# TEST on Local

# Basic Card
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "card_type": "basic",
        "title": "Basic Card",
        "subtitle": "This is a basic card.",
        "formatted_text": "Hello, World!",
        "image_url": "https://www.example.com/image.png",
        "image_alt_text": "Example Image"
      }' \
  http://localhost:5000/card

# Button Card
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "card_type": "button",
        "title": "Button Card",
        "subtitle": "This is a button card.",
        "formatted_text": "Hello, World!",
        "image_url": "https://www.example.com/image.png",
        "image_alt_text": "Example Image",
        "button_text": "Click me!",
        "button_url": "https://www.example.com"
      }' \
  http://localhost:5000/card


# Confirmation Card
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "card_type": "confirmation",
        "title": "Confirmation Card",
        "subtitle": "This is a confirmation card.",
        "formatted_text": "Do you want to proceed?",
        "image_url": "https://www.example.com/image.png",
        "image_alt_text": "Example Image",
        "confirm_button_text": "Yes",
        "deny_button_text": "No"
      }' \
  http://localhost:5000/card


# Chart Card
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "card_type": "chart",
        "title": "Chart Card",
        "subtitle": "This is a chart card.",
        "chart_data": {
            "data": [
                {"label": "A", "value": 10},
                {"label": "B", "value": 20},
                {"label": "C", "value": 30},
                {"label": "D", "value": 40},
                {"label": "E", "value": 50}
            ]
        }
      }' \
  http://localhost:5000/card

# List Card
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "card_type": "list",
        "title": "List Card",
        "subtitle": "This is a list card.",
        "items": [
            {"text": "Item 1", "image_url": "https://www.example.com/image1.png", "image_alt_text": "Example Image 1"},
            {"text": "Item 2", "image_url": "https://www.example.com/image2.png", "image_alt_text": "Example Image 2"},
            {"text": "Item 3", "image_url": "https://www.example.com/image3.png", "image_alt_text": "Example Image 3"},
            {"text": "Item 4", "image_url": "https://www.example.com/image4.png", "image_alt_text": "Example Image 4"},
            {"text": "Item 5", "image_url": "https://www.example.com/image5.png", "image_alt_text": "Example Image 5"}
        ]
      }' \
  http://localhost:5000/card


```

## Python code Example

```python

# basic_card
title = "Title"
subtitle = "Subtitle"
formatted_text = "This is some formatted text."
image_url = "https://example.com/image.jpg"
image_alt_text = "Alt text for the image."

basic_card = create_basic_card(title, subtitle, formatted_text, image_url, image_alt_text)


# button_card
title = "Title"
subtitle = "Subtitle"
formatted_text = "This is some formatted text."
image_url = "https://example.com/image.jpg"
image_alt_text = "Alt text for the image."
button_text = "Button Text"
button_url = "https://example.com/"

button_card = create_button_card(title, subtitle, formatted_text, image_url, image_alt_text, button_text, button_url)


# confirmation_card
title = "Title"
subtitle = "Subtitle"
formatted_text = "This is some formatted text."
image_url = "https://example.com/image.jpg"
image_alt_text = "Alt text for the image."
confirm_button_text = "Confirm"
deny_button_text = "Deny"

confirmation_card = create_confirmation_card(title, subtitle, formatted_text, image_url, image_alt_text, confirm_button_text, deny_button_text)


# chart_card
title = "Title"
subtitle = "Subtitle"
chart_data = {
    "title": "Chart Title",
    "chartData": {
        "labels": ["January", "February", "March", "April", "May"],
        "datasets": [
            {
                "label": "Dataset 1",
                "data": [10, 20, 30, 40, 50],
                "backgroundColor": "#4285F4"
            },
            {
                "label": "Dataset 2",
                "data": [50, 40, 30, 20, 10],
                "backgroundColor": "#DB4437"
            }
        ]
    },
    "chartType": "BAR",
    "legendPosition": "BOTTOM_LEGEND"
}

chart_card = create_chart_card(title, subtitle, chart_data)



# list_card
title = "Title"
subtitle = "Subtitle"
items = [
    {
        "text": "Item 1",
        "icon": {
            "imageUrl": "https://example.com/icon1.png"
        }
    },
    {
        "text": "Item 2",
        "icon": {
            "imageUrl": "https://example.com/icon2.png"
        }
    },
    {
        "text": "Item 3",
        "icon": {
            "imageUrl": "https://example.com/icon3.png"
        }
    }
]

list_card = create_list_card(title, subtitle, items)


```

```bash
curl -H "Content-Type: application/json" -X POST -d '{"title": "Basic Card", "subtitle": "This is a basic card", "text": "This is the body text of the basic card.", "image_url": "https://www.example.com/image.png", "alt_text": "Alt text for the image"}' http://localhost:8080/card/basic

curl -H "Content-Type: application/json" -X POST -d '{"title": "Button Card", "subtitle": "This is a button card", "text": "This is the body text of the button card.", "button_text": "Go to example.com", "button_url": "https://www.example.com"}' http://localhost:8080/card/button

curl -H "Content-Type: application/json" -X POST -d '{"title": "Confirmation Card", "subtitle": "This is a confirmation card", "text": "Are you sure you want to proceed?"}' http://localhost:8080/card/confirmation

curl -H "Content-Type: application/json" -X POST -d '{"title": "Chart Card", "subtitle": "This is a chart card", "chart_type": "LINE", "data_points": {"January": 10, "February": 20, "March": 30, "April": 40, "May": 50}}' http://localhost:8080/card/chart

curl -H "Content-Type: application/json" -X POST -d '{"title": "List Card", "subtitle": "This is a list card", "items": [{"text": "Item 1", "image_url": "https://www.example.com/image1.png", "image_alt_text": "Alt text for image 1"}, {"text": "Item 2", "image_url": "https://www.example.com/image2.png", "image_alt_text": "Alt text for image 2"}, {"text": "Item 3", "image_url": "https://www.example.com/image3.png", "image_alt_text": "Alt text for image 3"}]}' http://localhost:8080/card/list


```