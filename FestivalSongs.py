from telegram.ext import Updater
from telegram import InlineQueryResultArticle, InputTextMessageContent


updater = Updater(token='655307721:AAFlbYE4tJLZwWT84CgSyn1zOnGW9hWe_Q8')
dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=("Guten Tag " + update.message.from_user['first_name'] + "! :)"))


def song(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text ="The new song is:")

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text = update.message.text)


def caps(bot, update, args):
    print(args)
    if(args[0] == 'geheim'):
        bot.send_message(chat_id=update.message.chat_id, text='cant belive')
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text = text_caps)


def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)


from telegram.ext import CommandHandler, MessageHandler, Filters, InlineQueryHandler

echo_handler = MessageHandler(Filters.text, echo)
start_handler = CommandHandler('start', start)
song_handler = CommandHandler('song', song)
caps_handler = CommandHandler('caps', caps, pass_args=True)
inline_caps_handler = InlineQueryHandler(inline_caps)


dispatcher.add_handler(inline_caps_handler)
dispatcher.add_handler(song_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)



updater.start_polling()

