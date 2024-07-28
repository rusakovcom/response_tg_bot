import telebot
import requests

# Token from BotFather
BOT_TOKEN = ''

# Create a bot instance
bot = telebot.TeleBot(BOT_TOKEN)

# Check URL function
def get_response_code(url): # input in frormat 'example.com', https only
    x = requests.get(f'https://{url}/')
    return x.status_code # => 200, 500...
url = 'simpleone.ru'

# Checknow - Bot wait for 'checknow' and answer with status code for url (in BotFather /setcommands ; 'checknow - Check now')
@bot.message_handler(func=lambda message: message.text.lower() == '/checknow')
def send_status_code(message):
    bot.send_message(message.chat.id, get_response_code(url)) # this string send answer

# Start the bot
if __name__ == '__main__':
    print("Bot is running...")
    bot.polling()
