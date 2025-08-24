import telebot
from config import TG_TOKEN


bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.username}! Наша миссия состоит в том что - Мы помогаем сделать осознанное потребление доступным и практичным. Мы не призываем к идеалу — мы помогаем каждому найти свой путь к более экологичной жизни через понятные шаги, поддержку сообщества и акцент на личную пользу: здоровье, экономию и душевное спокойствие.')

        

bot.infinity_polling()
