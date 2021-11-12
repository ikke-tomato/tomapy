from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('sKnbqRQApoN2C6TW5/MSVM2/QB4w4tqojJf+qbq3V1G18VbbULl10eMWn+94qoWsUmbk92/j0ulF/v5rubGerfv5YJVhdkMjp4OuesInGAMTRQuGbg/HEQMKI6RMZKk2JuJYcbiRAiHambHYv0CHKwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4618cba20c09232e59c0a554dab4c645')

@app.route("/")
def test():
     return"OK"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="your message is " + event.message.text + " ."))
         

if __name__ == "__main__":
    app.run()