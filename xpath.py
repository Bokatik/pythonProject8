
from threading import Thread
import time

import requests
from lxml import html


def fridge_price(emt):
    url = f'https://franke-market.com.ua/{emt}'
    price_xPath = '/html/body/div[1]/div[1]/div[1]/div[9]/div/div[1]/div[2]/div[1]/div[2]/div/span/text()'
    name_xPath = '/html/body/div[1]/div[1]/div[1]/div[7]/div/h1/text()'
    code_xPath = '/html/body/div[1]/div[1]/div[1]/div[9]/div/div[1]/div[2]/div[1]/div[1]/div/span[1]/text()'
    response = requests.get(url)

    #print(response.status_code)

    tree = html.fromstring(response.text)
    price = tree.xpath(price_xPath)
    name = tree.xpath(name_xPath)
    code = tree.xpath(code_xPath)

    print(f'{code[0]} {name[0]}: {price[0]} грн.,')


# fridge_price('franke_1180606722')
# fridge_price('franke_1180606721')
# fridge_price('franke_1180606723')
# fridge_price('franke_1180629526')
# fridge_price('franke_1180627476')



# def ovens(emt):
#     url = f'https://franke-market.com.ua/{emt}'
#     price_xPath = '/html/body/div[1]/div[1]/div[1]/div[9]/div/div[1]/div[2]/div[1]/div[2]/div/span/text()'
#     name_xPath = '/html/body/div[1]/div[1]/div[1]/div[7]/div/h1/text()'
#     response = requests.get(url)
#
#     # print(response.status_code)
#
#     tree = html.fromstring(response.text)
#     price = tree.xpath(price_xPath)
#     name = tree.xpath(name_xPath)
#
#     print(f'{name[0]}: {price[0]} грн.')

# ovens('franke_1160606097')
# ovens('franke_1160606098')
# ovens('franke_fsl_86_h_bk_1160609447')
# ovens('franke_ma_86_m_bk_f_1160576979_vitrina')
# ovens('franke_1160606093')


names = ['franke_1180606722', 'franke_1180606721',
         'franke_1180606723', 'franke_1180629526', 'franke_1180627476',
         'franke_1160606097', 'franke_1160606098', 'franke_fsl_86_h_bk_1160609447']
start = time.perf_counter()
for name in names:
    fridge_price(name)
    end = time.perf_counter()
print(f'time wthout threads = {end - start:0.2f}')

start = time.perf_counter()
threads = []
for name in names:
    t = Thread(target=fridge_price, args=(name,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.perf_counter()
print(f'time with threads = {end - start:0.2f}')

