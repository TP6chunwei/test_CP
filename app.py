from flask import Flask, request, abort
import os
import requests
import json
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
    PostbackEvent, MemberJoinedEvent, LocationMessage
)

app = Flask(__name__)

# Channel Access Token and Secret (Note: These should ideally be stored securely, not hardcoded)
access_token = "QFVheezi84Iy1z9+jhHfMAQLG7W2qtfs2BJVn18HVxt96WxxLzdGXzbdycnGiXkUk7g3wn7LIdmXbzuo7+s2mUX4I99hf2xSCq4ysfAHK/c8kpug7Vq6k458Js+An0XVhvNENn9Km2OuHL5cFhU9YQdB04t89/1O/w1cDnyilFU="
channel_secret = "e752f446b5fd2237eaa8d61ae077ec93"
line_bot_api = LineBotApi(access_token)
handler = WebhookHandler(channel_secret)


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if  event.message.type == 'text':
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
       
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
