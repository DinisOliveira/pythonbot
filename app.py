#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot
import os 
app = Flask(__name__)
ACCESS_TOKEN = 'EAAKGgM6LgXoBADqhYTzq2VWkENwsghsErZBFzR1ovZAfu1SKdIVPxMSnMD2kxYgDcrpo6sIVAZBmQ7QYxS80fSDD6TFC6JgDa5O3ZB8QWZApRDdHNUuqSYWARDHArNagCX2ZAWGCeALZCTO4f6Swp8j6pGQxmYsxgenygq5V1CNxAZDZD'   #ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = 'cheese'   #VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot (ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route(API_ROOT + FB_WEBHOOK, methods=["GET"])
def fb_webhook():
    verification_code = 'I_AM_VERIFICIATION_CODE'
    verify_token = request.args.get('hub.verify_token')
    if verification_code == verify_token:
        return request.args.get('hub.challenge')


@app.route(API_ROOT + FB_WEBHOOK, methods=['POST'])
def fb_receive_message():
    message_entries = json.loads(request.data.decode('utf8'))['entry']
    for entry in message_entries:
        for message in entry['messaging']:
            if message.get('message'):
                print("{sender[id]} says {message[text]}".format(**message))
    return "Hi"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

    def check_for_greeting(sentence):
        """If any of the words in the user's input was a greeting, return a greeting response"""
        for word in sentence.words:
            if word.lower() in GREETING_KEYWORDS:
                return random.choice(GREETING_RESPONSES)
    # start:example-none.py
    # Sentences we'll respond with if we have no idea what the user just said
    NONE_RESPONSES = [
        "uh whatever",
        "meet me at the foosball table, bro?",
        "code hard bro",
        "want to bro down and crush code?",
        "I'd like to add you to my professional network on LinkedIn",
        "Have you closed your seed round, dog?",]

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()
