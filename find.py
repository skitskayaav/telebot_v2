from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
from PIL import Image

class Find:
    def __init__(self, driver):
        self.driver = driver 
        self.name = ''
    def Name(self, name):
        self.name = name
        
    def findbyname(self):  #информация о фильме
        self.driver.get('https://www.film.ru/') #заходим на сайт
        search_input = self.driver.find_element_by_xpath('//*[@id="quick_search_input"]') #ищем поисковую строку
        search_input.send_keys(f'{self.name}' + Keys.RETURN) #вводим запрос в поисковую строку
        try:
            self.driver.find_element_by_xpath('//*[@id="movies_list"]/a[1]').click() #первый фильм из списка
            film = self.driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div[1]/div[1]/div[3]/h1').text
            self.discr = self.driver.find_element_by_xpath('//*[@id="movies-1"]/div/p').text
            self.year = self.driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div[1]/div[1]/div[3]/h3').text.split(',')[0]
            self.howlong = self.driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div[1]/div[1]/div[3]/div[1]/div[1]/strong').text
            img = self.driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div[1]/div[1]/div[2]/a/img')
            src = img.get_attribute('src')
            urllib.request.urlretrieve(src, "film_pic.png")
        except: 
            pass
    
    
    def filmslikethis(self): #похожие фильмы на введенный
        films = []
        self.driver.get('https://www.kinopoisk.ru')
        films_element = self.driver.find_element_by_name("kp_query")
        films_element.send_keys(self.name + Keys.RETURN)
        self.driver.find_element_by_xpath('//*[@id="block_left_pad"]/div/div[2]/div/div[2]/p/a').click()
        s = self.driver.current_url
        s = s.replace('series', 'film')
        self.driver.get(f'{s}/like/')
        for i in range(5):
            try:
                name = self.driver.find_elements_by_xpath(f'/html/body/main/div[4]/div[1]/table/tbody/tr/td[1]/div/table[1]/tbody/tr/td/table[2]/tbody/tr[{i}]/td[2]/div')
                for j in name:
                    s = j.text.replace('...', '')
                    k = s.rindex(')', 0, len(s))+1
                    films.append(s[:k:])
            except:
                pass
            self.like = films
    
    
    
    def cinemas(self, city): #кинотеатры
        self.driver.get('https://www.google.com/')
        search_input = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input') #поисковая строка
        st = 'кинотеатр ' + f'{self.name} ' + f'{city}'#вводит запрос
        search_input.send_keys(st +Keys.RETURN)
        try:
            self.driver.find_element_by_xpath('//*[@id="rso"]/div[2]/div/div/div[1]/a/h3').click() #заходит на первую ссылку
        except:
            pass
        url = self.driver.current_url
        self.afisha = url 
    
    
    def findalso(self, genre): #подборки фильмов
        self.genre = genre
        films = []
        self.driver.get('https://www.google.ru')
        films_element = self.driver.find_element_by_name("q") #поисковая строка
        films_element.send_keys(f'иви подборка {self.genre}' + Keys.RETURN)
        try:
            self.driver.find_element_by_class_name('truncation-information').click() 
        except:
            try:
                self.driver.find_element_by_xpath('/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/a/h3').click()
            except:
                self.driver.find_element_by_xpath('/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/a/h3').click() #
        self.driver.switch_to.window(self.driver.window_handles[1]) #переходим во вкладку
        item = self.driver.find_elements_by_class_name('nbl-slimPosterBlock__title')
        for i in range(5):
            films.append(item[i].text)
        self.podbor = films
  

    def Sound(self):
        self.driver.get('https://www.kinopoisk.ru')
        films_element = self.driver.find_element_by_name("kp_query")
        films_element.send_keys(self.name + Keys.RETURN)
        self.driver.find_element_by_xpath('//*[@id="block_left_pad"]/div/div[2]/div/div[2]/p/a').click()
        s = self.driver.current_url
        s = s.replace('series', 'film')
        self.driver.get(f'{s}/tracks/')
        try:
            if (self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/h1').text == '404. Страница не найдена'):
                return 'саундтреков нет :('
        except:
            self.sound = self.driver.current_url
