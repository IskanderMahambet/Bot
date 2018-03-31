import telebot

person_info={'ВИКТОР':'+77777777777',
             'НУРБОЛ':'+77072344565',
             'ИСКАНДЕР':'+77024162892'}

token = '485606860:AAFC1eSP_LksyJSRHsDK0Z9b49Rt4u_YzEI'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def check_message(message):

    name = message.text

    name=name.upper()
    if name in person_info:
        bot.send_message(message.chat.id, person_info[name])
    else:
        bot.send_message(message.chat.id, 'Такого имени нет')

bot.polling(none_stop=True)
