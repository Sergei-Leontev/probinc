# probinc
import telebot
from chopi import keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'что бы начать рабату надо вводить команды так: \n<название валюты› \‹в какую валюту надо перевести> \ <количество валюты которую хотите перевести>\n узнать все доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=[' values'])
def values(message: telebot.types.Message):
    text = 'доступные на данный момент валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('много параметров.')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as a:
        bot.reply_to(message, f'ОШИБКА пользователя\n{a}')
    except Exception as a:
        bot.reply_to(message, f'не удолось распознать команду\n{a}')
    else:
        text = f'цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()
