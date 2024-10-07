from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = '7869919667:AAEWkT-df4-MyMso0murmfhQ_9iB-s7w3zY'

button_texts = {
    'Кнопка 1': 'Вы нажали на Кнопку 1',
    'Кнопка 2': 'Вы нажали на Кнопку 2',
    'Кнопка 3': 'Вы нажали на Кнопку 3',
    'Кнопка 4': 'Вы нажали на Кнопку 4',
    'Кнопка 5': 'Вы нажали на Кнопку 5',
    'Кнопка 6': 'Вы нажали на Кнопку 6',
    'Кнопка 7': 'Вы нажали на Кнопку 7',
    'Кнопка 8': 'Вы нажали на Кнопку 8',
    'Кнопка 9': 'Вы нажали на Кнопку 9',
    'Кнопка 10': 'Вы нажали на Кнопку 10',
    'Кнопка 11': 'Вы нажали на Кнопку 11',
    'Кнопка 12': 'Вы нажали на Кнопку 12',
}


def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        ['Кнопка 1', 'Кнопка 2', 'Кнопка 3'],
        ['Кнопка 4', 'Кнопка 5', 'Кнопка 6'],
        ['Кнопка 7', 'Кнопка 8', 'Кнопка 9'],
        ['Кнопка 10', 'Кнопка 11', 'Кнопка 12']
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=False, resize_keyboard=True)

    update.message.reply_text(
        'Выберите одну из кнопок:', reply_markup=reply_markup)


def button_handler(update: Update, context: CallbackContext) -> None:
    user_choice = update.message.text

    if user_choice in button_texts:
        update.message.reply_text(button_texts[user_choice])
    else:
        update.message.reply_text(
            "Пожалуйста, выберите одну из доступных кнопок.")
    start(update, context)


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, button_handler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
