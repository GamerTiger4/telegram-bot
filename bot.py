import telebot
from flask import Flask, request

API_TOKEN = "7796810242:AAGnh-MKHOjreMzWud9NwE0pArJVMwzg9yw"
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route(f"/{API_TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@app.route("/")
def home():
    return "Bot is running!", 200

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! ربات من روی Render فعاله ✅")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)