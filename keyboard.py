from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

class Keyboard:
    def makekeybrd(self): #создание клавиатуры
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(InlineKeyboardButton('Помощь', callback_data = 'help'),  #добавление кнопок
                   InlineKeyboardButton('Прислать информацию о фильме', callback_data = 'send_film'),
                   InlineKeyboardButton('Прислать похожий фильм', callback_data = 'send_another'),
                   InlineKeyboardButton('Купить билет в кино', callback_data = 'buy'),
                   InlineKeyboardButton('Прислать подборку', callback_data = 'also'),
                   InlineKeyboardButton('Прислать саундтреки', callback_data = 'sound'),
                   InlineKeyboardButton('Перейти к новому фильму', callback_data = 'new')
                  )
        return markup
