import telebot
class Bot:
    def __init__(self): #конструктор бота
        self.bot = telebot.TeleBot(token)
        self.film = Find(webdriver.Chrome()) 
        
        
    def keyboard(self):
        @self.bot.message_handler(content_types = ['sticker'])
        def get_text_message(message):
            m = Keyboard()
            markup = m.makekeybrd()
            self.bot.send_message(message.chat.id, text = "привет, смотри, что я могу!!", reply_markup = markup)
                
    def send_info(self, message):
        if (self.film.name == ''):
            self.film.Name(message.text)
        self.film.findbyname()
        self.bot.send_message(message.chat.id, f'Название фильма - {self.film.name}, год выпуска - {self.film.year}, {self.film.howlong}\n{self.film.discr}')
        photo = open('film_pic.png', 'rb')
        self.bot.send_photo(message.chat.id, photo)  
      
    
    def send_buy(self, message):
        if (self.film.name == ''):
            s = message.text.split('-')
            self.film.Name(message.text[0])
            self.film.Name(s[0])
            self.film.cinemas(s[1])
        else:
            self.film.cinemas(message.text)
        self.bot.send_message(message.chat.id, self.film.afisha)

        
    def send_also(self, message):
        self.film.findalso(message.text)
        for i in range(len(self.film.podbor)):
            self.bot.send_message(message.chat.id, self.film.podbor[i])
        
        
    def send_sound(self, message):
        if (self.film.name == ''):
            self.film.Name(message.text)
        self.film.Sound()
        self.bot.send_message( message.chat.id, self.film.sound)
    
    
    def send_another(self, message):
        if (self.film.name == ''):
            self.film.Name(message.text)
        self.film.filmslikethis()
        for i in range(len(self.film.like)):
            self.bot.send_message(message.chat.id, self.film.like[i])
    
    
    def answer(self): #отвечает на запросы
        @self.bot.callback_query_handler(func = lambda call: True)
        def query_handler(call):
            self.bot.answer_callback_query(callback_query_id = call.id)
            answer = ''
            
            if (call.data == 'help'):
                answer = 'Привет! Я могу прислать тебе информацию о фильме (год выпуска, рейтинг, описание), найти похожее, на то что тебе понравилось и кинуть ссылочку, где можно купить билеты в кино!'
                self.bot.send_message(call.message.chat.id, answer)
            
            if (call.data == 'send_film'):
                if (self.film.name == ''):
                    answer = 'Пришли название фильма/сериала/мультфильма'
                else:
                    answer = 'Если хочешь перейти к новому фильму нажми на кнопку "Перейти к новому фильму", иначе пришли "Нет"'
                self.bot.send_message(call.message.chat.id, answer)
                self.bot.register_next_step_handler(call.message, self.send_info)
 
            if (call.data == 'send_another'):
                if (self.film.name == ''):
                    answer = 'Пришли название фильма/сериала, я подберу похожий!'
                else:
                    answer ='Если хочешь перейти к новому фильму нажми на кнопку "Перейти к новому фильму", иначе пришли "Нет"'
                self.bot.send_message(call.message.chat.id, answer)
                self.bot.register_next_step_handler(call.message, self.send_another)
                        
            if (call.data == 'buy'):
                if (self.film.name == ''):
                    answer = 'На что хочешь пойти? Введи, пожалуйста, через тире название фильма и город'
                else:
                    answer = 'Пришли, пожалуйста, название города'
                self.bot.send_message(call.message.chat.id, answer)
                self.bot.register_next_step_handler(call.message, self.send_buy)
            
            if (call.data == 'also'):
                answer = 'Какую подборку прислать?'
                self.bot.send_message(call.message.chat.id, answer)
                self.bot.register_next_step_handler(call.message, self.send_also)
            
            if (call.data == 'sound'):
                if (self.film.name == ''):
                    answer = 'Введи название фильма'
                else:
                    answer = 'Если хочешь перейти к новому фильму нажми на кнопку "Перейти к новому фильму", иначе пришли "Нет"'
                self.bot.send_message(call.message.chat.id, answer)
                self.bot.register_next_step_handler(call.message, self.send_sound)
               
                
            if (call.data == 'new'):
                self.film.driver.close()
                self.film = Find(webdriver.Chrome())
                answer = 'тыкни еще раз на нужную тебе кнопку'
                self.bot.send_message(call.message.chat.id, answer)

                
    def run_bot(self):
        self.keyboard()
        self.answer()
        self.bot.polling()
        
tel = Bot()
tel.run_bot()
