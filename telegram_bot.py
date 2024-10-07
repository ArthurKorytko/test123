from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '7869919667:AAECA4RGJoBPQMBK4rdm1PTrngOpxwq9ttw'

button_texts = {
    'Оксененко С.А': 'ZOOM: \n Логин: 9184322138 \n Пароль: 2sKy8e',
    'Панова О.С.': 'ZOOM: \n Логин: 938 958 8159 \n Пароль: 401',
    'Мілютіна О. С.': 'ZOOM: \n Логин: 978 357 9002 \n Пароль: 211047',
    'Семенченко Т. О': 'ZOOM: \n Логин: 764 968 7132 \n Пароль: 507',
    'Іванова І.В.': 'ZOOM: \n Логин: 986 034 2218 \n Пароль: 311',
    'Каплун Є.О.': 'ZOOM: \n Логин: 5068639210 \n Пароль: 1723',
    'Бєлікова В.В.': 'ZOOM: \n Логин: 5742475269 \n Пароль: 235067',
    'Ігнатьєв Д.С.': 'Google Meet: \n https://meet.google.com/rdo-wrez-vci',
    'Бєлікова С.О': 'ZOOM: \n Логин: 484 982 3188 \n Пароль: 12345',
    'Повгородній В.О.': 'Google Meet: \n https://meet.google.com/cmg-hhvv-fqw',
    'Онопченко А.В.': 'Google Meet: \n https://meet.google.com/fmg-avfj-byp?authuser=2',
    'Кто что ведет?': 'ТО ЕТ ЕЛ Лк - Бєлікова С.О. \n ОПрогр - Ігнатьєв Д.С. \n ІсторіяУ - Панова О.С. \n ВМатем - Мілютіна О. С \n Фізика ЛК - Семенченко Т.О. \n Фізика ПЗ - Повгородній В.О. \n Фізика Лб - Онопченко А.В \n ФізВихов - Каплун Є.О \n IT ЛК - Бєлікова В.В. \n ІТ ЛБ - Іванова І.В. \n ЕконТ-рія - Оксененко С.А',
    'Время пар': '1 пара: 8:30 - 9:50 \n2 пара: 10:00 - 11:20 \n3 пара: 11:40 - 13:00 \n4 пара: 13:10 - 14:30 \n5 пара: 14:40 - 16:00 \n6 пара: 16:10 - 17:30 \n7 пара: 17:40 - 19:00',
    'Дополнительная информация': 'Мой создатель: @ArthurKorytko \nЕсли какие-то ошибки, или дополнения, пиши ему.',
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        ['Оксененко С.А', 'Панова О.С.', 'Мілютіна О. С.'],
        ['Семенченко Т. О', 'Іванова І.В.', 'Каплун Є.О.'],
        ['Бєлікова В.В.', 'Ігнатьєв Д.С.', 'Бєлікова С.О.'],
        ['Повгородній В.О.', 'Онопченко А.В.', 'Кто что ведет?'],
        ['Время пар', 'Дополнительная информация']
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=False, resize_keyboard=True)
    await update.message.reply_text('Какая пара тебя интересует?', reply_markup=reply_markup)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_choice = update.message.text

    if user_choice in button_texts:
        await update.message.reply_text(button_texts[user_choice])
    else:
        await update.message.reply_text("Выбери одного из преподователей что бы узнать инфомацию о ссылке на пару")


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, button_handler))
    application.run_polling()


if __name__ == '__main__':
    main()
