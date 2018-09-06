

import os, sys
from flask import Flask, request
from utils import wit_response
from pymessenger import Bot
import pytube


app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAKGgM6LgXoBADgbp5DZCrYHf9tos0bHmSE2hoEoAorEkDOZAT1K45OddBaSSTvBLre5Y2rjCCcNZAF6lUd77aHmWhA4rk4Oj0A6W5evsXhQOubEyHcXWHAmOIrXg9JjyE5dJpegOSBaYJYKXrV8k2eObyZC4c6QmJhmmrTnqwZDZD"
bot = Bot(PAGE_ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
    # Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "cheese":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

                # Ids
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no text'

                    response = None
                    entity, value = wit_response(messaging_text)

                    if entity == 'newstype':
                        response = "Ok I will send you {} news".format(str(value))
                    elif entity == "location":
                        response = "Ok, So, you live in {0}. I will send you top headlines from {0}".format(str(value))

                    if response is None:
                        response = "Sorry I did not understand"
                        bot.send_text_message(sender_id, response)

    return "ok", 200


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(debug=True, port=80)
