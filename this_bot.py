import telebot
import function_students

token = '485606860:AAFC1eSP_LksyJSRHsDK0Z9b49Rt4u_YzEI'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def check_message(message):
    if message.text == 'Список студентов':
        for student in function_students.get_list_students():            
            bot.send_message(message.chat.id,student)
    elif message.text == 'Сред. оценка':
        bot.send_message(message.chat.id,function_students.get_aver_students_mark())
    elif message.text.isdigit():
       bot.send_message(message.chat.id,'Имя: '+function_students.get_student_by_num(int(message.text)[0]))
       bot.send_message(message.chat.id,'Оценка: '+function_students.get_student_by_num(int(message.text)[1]))
    else:
       bot.send_message(message.chat.id, 'Студента с данным номерон не существует')

bot.polling(none_stop=True)
