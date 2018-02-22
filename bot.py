import telebot
from jenkins import Jenkins
from datetime import datetime
from configuration import configure_build, servers


server = Jenkins('http://234234', username='234234', password='234234')


bot_token = '2434234'
bot = telebot.TeleBot(bot_token)


@bot.message_handler(content_types=["text"])
def build(message):
    if message.text == '/start':
        text = """
        """
        bot.send_message(message.chat.id, text)
    else:
        try:
            bot.send_message(message.chat.id, "Wait a second, bro")
            print(message.from_user.username,
                  message.from_user.first_name, message.from_user.last_name,
                  message.text)
            with open('botlog.log', 'a', encoding='utf-8') as log:
                timestamp = datetime.now()
                log.write('{} {} {} {} {} \n'.format(timestamp,
                                                     message.from_user.username,
                                                     message.from_user.first_name,
                                                     message.from_user.last_name,
                                                     message.text))
            server_settings = servers[message.text]
            job_settings = configure_build(server_settings[0], server_settings[1])
            server.build_job('Roundme.Full.Build', job_settings)
            bot.send_message(message.chat.id, "Job started: {} with branch {}".format(server_settings[0],
                                                                                      server_settings[1]))
        except KeyError:
            bot.send_message(message.chat.id, 'I dont know {}'.format(message.text))


if __name__ == '__main__':
    bot.polling(none_stop=True)