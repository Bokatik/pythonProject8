

import requests
from lxml import html


import sqlite3

# создание таблицы
def create_fridges():
    connect = sqlite3.connect('franke_data_base.db')
    cursor = connect.cursor()

    cursor.execute("CREATE TABLE users (name TEXT, price TEXT)")
    connect.commit()


# добавление данных в таблицу
def add_fridge(fridge: dict):
    connect = sqlite3.connect('franke_data_base.db')
    cursor = connect.cursor()
    request_in_fridge = f'INSERT INTO users (name, price) VALUES ("{fridge["name"]}", "{str(fridge["price"])}");'
    print(request_in_fridge)
    cursor.execute(request_in_fridge)
    connect.commit()


def fridge_price():
    url = f'https://franke-market.com.ua/ua/shop/holodilniki'
    for i in range(1, 13):
        response = requests.get(url)
        index = 0
        if response.status_code == 200:
            tree = html.fromstring(response.text)
            names = []
            prices = []
            for idx in range(1, 13):
                name_xPath = f'/html/body/div[1]/div[1]/div[1]/div[9]/div/div/div[2]/div[1]/' \
                             f'div[3]/div[{index}]/div/div/a[1]/div/div[2]/text()'
                price_xPath = f'/html/body/div[1]/div[1]/div[1]/div[9]/div/div/div[2]/div[1]' \
                              f'/div[3]/div[{index}]/div/div/div[2]/span/text()'

                name = tree.xpath(name_xPath)
                price = tree.xpath(price_xPath)
                if (len(name) > 0):
                    names.append(name[0])
                    prices.append(price[0])
                else:
                    print(name, price)
                index += 1
            for idx in range(len(prices)):
                print(f'{str(idx + 1)}: {names[idx]}, price:{prices[idx]}грн.')
                add_fridge({"name": names[idx], "price": prices[idx]})


# получение данных из таблицы
def get_fridge(name):
    connect = sqlite3.connect('franke_data_base.db')
    cursor = connect.cursor()
    get = f'SELECT name, price FROM users WHERE name="{name}"'
    cursor.execute(get)
    # метод fetchall возвращает список кортежей с заданными значениями
    result = cursor.fetchall()
    print(result)
    cursor.close()