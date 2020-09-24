from telegram.ext import Updater, CommandHandler
import requests   

def get_url():
    contents= requests.get('https://random.dog/woof.json').json()
    url= contents['url']
    return url

def dog(bot, update):
    url= get_url()
    chat_id= update.message.chat_id
    bot.send_photo(chat_id, photo=url)   

u= Updater('access_token')
dp= u.dispatcher
dp.add_handler(CommandHandler('dog', dog))
u.start_polling()
u.idle()
