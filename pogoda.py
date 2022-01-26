# Импортируем все из библиотеки TKinter
from tkinter import *

# Эта библиотека нужна для работы с отправкой URL запросов
from tkinter import Frame

import requests

# Создаем главный объект (по сути окно приложения)
root = Tk()


# Эта функция срабатывает при нажатии на кнопку "Посмотреть погоду"
def get_weather():
    # Cоздаем фрейм куда будут выводиться данные
    frame_bottom = Frame(root, bg='#ffb700', bd=5)
    frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

    # Создаем текстовую надпись, в которую будет выводиться информация о погоде
    info = Label(frame_bottom,  bg='#ffb700', font=40)
    info.pack()
    # Получаем данные от пользователя
    city = cityField.get()

    # данные о погоде будем брать с сайта openweathermap.org
    # ниже пропишите свой API ключ, который получите в кабинете пользователя на сайте openweathermap.org
    key = '2caaa379dcae46f13bc235371ee1224e'
    # key = '56b30cb255.3443075'
    # ссылка, с которой мы получим все данные в формате JSON
    url = 'http://api.openweathermap.org/data/2.5/weather'
    #url = 'https://api.gismeteo.net/v2/weather/current/4368/'
    # Дополнительные парамтеры (Ключ, город введенный пользователем и единицины измерения - metric означает Цельсий)
    params = {'APPID': key, 'q': city, 'units': 'metric', 'lang': 'ru'}
    # Отправляем запрос по определенному URL
    result = requests.get(url, params=params)
    # Получаем JSON ответ по этому URL
    weather = result.json()

    # Полученные данные добавляем в текстовую надпись для отображения пользователю
    info['text'] = f'{str(weather["name"])}: Температура {weather["main"]["temp"]} Видимость: {str(weather["visibility"])} метров'
    print(weather)

# Настройки главного окна

# Указываем фоновый цвет
root['bg'] = '#fafafa'
# Указываем название окна
root.title('Погодное приложение')
# Указываем размеры окна
root.geometry('300x250')
# Делаем невозможным менять размеры окна
root.resizable(width=True, height=True)

# Создаем фреймы (область для размещения других объектов)
frame_top2 = Frame(root, bg='#05fcfc', bd=5, relief =RAISED)
frame_top2.place( relwidth=1, relheight=1)

# Указываем к какому окну он принадлежит, какой у него фон и какая обводка
frame_top = Frame(root, bg='#ffb700', bd=5)
# Также указываем его расположение
frame_top.place(relx=0.15, rely=0.20, relwidth=0.7, relheight=0.3)
title = Label(frame_top2, text='Введите название  \n населенного пункта',  bg= 'Cyan', font= ('inpact','14'))
title.pack()
# Создаем текстовое поле для получения данных от пользователя
cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()  # Размещение этого объекта, всегда нужно прописывать

# Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()



# Запускаем постоянный цикл, чтобы программа работала
root.mainloop()