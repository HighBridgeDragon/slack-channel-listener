import os 
from dotenv import load_dotenv
from slack_bolt import App

load_dotenv(dotenv_path=r".env")

# ボットトークンと署名シークレットを使ってアプリを初期化します
app = App(
    token=os.getenv(r"SLACK_BOT_TOKEN"),
    signing_secret=os.getenv(r"SLACK_SIGNING_SECRET")
)

# 'hello' を含むメッセージをリッスンします
@app.message(r"hello")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(f"Hey there <@{message['user']}>!")

# appに関連づけられたbotに対するメンションイベントを処理します
@app.event(r"app_mention")
def read_mention_message(event, say):
    text = event[r"text"]
    say("{0}".format(text))

# アプリを起動します
if __name__ == r"__main__":
    app.start(port=int(os.environ.get(r"PORT", 3000)))