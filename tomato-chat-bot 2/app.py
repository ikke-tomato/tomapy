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

line_bot_api = LineBotApi('rJx7ygh+drEY5jR7wTnXSc3eF0ZIvEJzjTDT7qo0/xoj6IxOpFLC5DL9Q9BFBNNbUmbk92/j0ulF/v5rubGerfv5YJVhdkMjp4OuesInGAN8iPz/LIeGvdfU70QHg73whwCv0uYVa31Jz5m0tpqQbgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4618cba20c09232e59c0a554dab4c645')

@app.route("/")
def test():
    return "OK"
    
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

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()