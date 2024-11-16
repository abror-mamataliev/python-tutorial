from telebot import TeleBot

bot = TeleBot("<TOKEN>")


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == "__main__":
    bot.polling()
