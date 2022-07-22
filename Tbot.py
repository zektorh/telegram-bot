import telebot



TOKEN = '5519064364:AAFWHRLYF0NW5J3Wvr68xSfVBvuIW7RC24s'


bot = telebot.TeleBot(TOKEN)

bot.message_handler(commands=['start'])
def starts(message):
    bot.reply_to(message, "این ربات ساخته ی حسین عظیمی است و هرچیزی را به انگلیسی بنویسی را به ایدی تلگرام تبدیل میکنه")


@bot.message_handler(func= lambda m: True)

def b(message):
    x = f"https://t.me/{message.text}"
    bot.reply_to(message, x)

    if message.text == "/start":
        starts(message)
    else:
        pass
    
bot.infinity_polling()