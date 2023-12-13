# -*- coding: cp1251 -*-
import requests
import fake_useragent
from bs4 import BeautifulSoup                                                                                
import threading, time
import random
from collections import Counter
import apehaBot_tme



session = requests.Session()
apeha = "https://kovcheg2.apeha.ru/"
link = "https://kovcheg2.apeha.ru/index.shtml"
user = fake_useragent.UserAgent().random
header = {
    'user-agent': user
}
data = {
    'actUser-Login': '1',
    'login': 'CubaDaleko',
    'pwd' : 'kojlbt11'
}
def vremia ():
    t = time.localtime() 
    current_time = time.strftime("%H:%M:%S", t) 
    print(current_time)
    return current_time
lap = 0
responce = session.post(link, data=data, headers=header).text

src_start = responce.find("newWin")
src_end = responce.find("\"",src_start)
src_tri = responce.find("\"",src_end+1)
src = ""
for n in range(src_end + 1, src_tri):
    src = src + responce[n]

link_newwin = str((src))
enter_responce = session.get(link_newwin, headers=header).text

# маг магаз
def mag_magaz ():
    link_magshop = "https://kovcheg2.apeha.ru/mageshop.html"
    responce = session.get(link_magshop, headers=header).text5е
    print("Перешли в маг магаз")
    time.sleep(random.randint(1, 3))
    return responce
# данные для посылки входа в алтарь Куба заклинателя
cuba = {
    'unick': 'CubaDaleko'
}
# Куба заклинатель переход
def mag_cuba ():
    link_cuba = "https://kovcheg2.apeha.ru/magiccasters.html"
    responce = session.post(link_cuba, data=cuba, headers=header).text
    # print("Перешли в алтарь Куба")
    # time.sleep(random.randint(1, 3))
    return responce
# пока оставим но возможно можно будет удалить
cubamag_responce = mag_cuba()

def work (responce):
    src_cp = responce.find("Работать")
    return src_cp

def work_start (responce):
    src_cp = responce.find("Работать")
    src_cp_start = responce.find("\'m", src_cp)
    return src_cp_start

def work_end (responce):
    src_cp = responce.find("Работать")
    src_cp_start = responce.find("\'m", src_cp)
    src_cp_end = responce.find("\'", src_cp_start + 1)
    return src_cp_end

src_if = ""
for n in range(work(mag_cuba()), work(mag_cuba()) + 8):
    src_if = src_if + cubamag_responce[n]
m = 0
apehaBot_tme.get_text_messages(src_if, apehaBot_tme.chat_id)
print(src_if)
while src_if == "Работать":
    cubamag_responce = mag_cuba()
    src_if = ""
    for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
        src_if = src_if + cubamag_responce[n]
    src_1 = ""
    for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
        src_1 = src_1 + cubamag_responce[n]

    link_work = apeha + src_1
    work_responce = session.get(link_work, headers=header).text

    src_2 = ""
    src_rab = src_1.find(".")
    for n in range(0, src_rab):
        src_2 = src_2 + src_1[n]

    src_3 = ""
    src_wait = work_responce.find("Осталось отдыхать")
    src_time = work_responce.find(":", src_wait)
    for n in range(src_time + 6, src_time + 13):
        src_3 = src_3 + work_responce[n]
    print(src_3)

    src_data_work = ""
    src_rab_data = src_1.find("reqid")
    for n in range(src_rab_data + 6, src_rab_data + 14):
        src_data_work = src_data_work + src_1[n]
    work_data = {
        'jobid': src_data_work,
        'actUser-StartWork' : '42'
    }
    # src_work = ""
    if src_wait == -1:
        print("Заебумба можно работать")
        time.sleep(random.randint(1, 2))
        link_back = apeha + src_2 + ".html"
        back_responce = session.post(link_back, data=work_data, headers=header).text      
        time.sleep(random.randint(10, 25))

        # маг магаз
        mag_responce = mag_magaz()
        time.sleep(random.randint(4, 13))
        cubamag_responce = mag_cuba()

        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        link_work = apeha + src_1
        work_responce = session.get(link_work, headers=header).text

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print("Заебумба отработал дальше отдых: " + src_3)  
        time.sleep(random.randint(1, 2))
        apehaBot_tme.get_text_while("Заебумба отработал дальше отдых: " + src_3, apehaBot_tme.chat_id)
        lap += 1
        print("Закляли - " + str(lap))
        time.sleep(random.randint(1, 2))
        apehaBot_tme.get_text_while("Закляли - " + str(lap) +" шмоток - " + src_3 + " в - " + vremia(), apehaBot_tme.chat_id)
    else:
        print(src_3)
        print(src_1)
        print("Ждем 1,5 часа")
        time.sleep(random.randint(1, 2))
        apehaBot_tme.get_text_while("Уставший - " + src_3 + " в - " + vremia(), apehaBot_tme.chat_id)
        vremia()
        time.sleep(random.randint(332, 405))


        print("Кладем шмотку на альтарь")
# кладем на алтарь
        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]
        # print(src_1)
        src_altar = ""
        src_altar = cubamag_responce.find("Выберите предмет")
        src_altar_start = cubamag_responce.find("e=", src_altar+16)

        work_responce = session.get(link_work, headers=header).text
        time.sleep(random.randint(5, 9))

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        altar = ""
        for n in range(src_altar_start + 3, src_altar_start + 12):
            altar = altar + cubamag_responce[n]
        # print(altar)
        print("Кладем шмотку на алтарь")
        altar_data = {
            'itemid': altar
        }       
        link_work = apeha + src_2 + ".html"
        print(link_work)
        altar_responce = session.post(link_work, data=altar_data, headers=header).text
        print(altar_data)
        print(altar_responce)
        time.sleep(random.randint(1, 2))
        apehaBot_tme.get_text_while("Положили шмотку на Альтарь", apehaBot_tme.chat_id)
# закончили класть
        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        link_work = apeha + src_1
        work_responce = session.get(link_work, headers=header).text

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print(src_3)
        print("Прошло 200")
        vremia()  
        apehaBot_tme.get_text_while("Прошло 200 - " + src_3 + " в - " + vremia(), apehaBot_tme.chat_id)    
        time.sleep(random.randint(555, 585))

        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        link_work = apeha + src_1
        work_responce = session.get(link_work, headers=header).text

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print(src_3)
        print("Прошло 700")
        vremia()  
        apehaBot_tme.get_text_while("Прошло 700 - " + src_3 + " в - " + vremia(), apehaBot_tme.chat_id)    
        time.sleep(random.randint(525, 575))

        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        link_work = apeha + src_1
        work_responce = session.get(link_work, headers=header).text

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print(src_3)
        print("Прошло 1200")
        vremia()  
        apehaBot_tme.get_text_while("Прошло 1200 - " + src_3 + " в - " + vremia(), apehaBot_tme.chat_id)    
        time.sleep(random.randint(545, 565))        


        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        link_work = apeha + src_1
        work_responce = session.get(link_work, headers=header).text

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print(src_3)
        print("Прошло 1700 - ")
        vremia()  
        apehaBot_tme.get_text_while("Прошло 1700 - " + src_3 + " в - " + vremia(), apehaBot_tme.chat_id)    
        time.sleep(random.randint(515, 525))

        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        link_work = apeha + src_1
        work_responce = session.get(link_work, headers=header).text

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print(src_3)
        print("Прошло 2200 - ")
        vremia()  
        apehaBot_tme.get_text_while("Прошло 2200 - " + src_3 + " в - " + vremia(), apehaBot_tme.chat_id)    
        time.sleep(random.randint(555, 585))


        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        link_work = apeha + src_1
        work_responce = session.get(link_work, headers=header).text

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print(src_3)
        print("Прошло 2700 - ")
        vremia()  
        apehaBot_tme.get_text_while("Прошло 2700 - " + src_3 + " в - " + vremia(), apehaBot_tme.chat_id)    
        time.sleep(random.randint(555, 585))

        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        link_work = apeha + src_1
        work_responce = session.get(link_work, headers=header).text

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print(src_3)
        print("Прошло 3200 - ")
        vremia()  
        apehaBot_tme.get_text_while("Прошло 3200 - " + src_3 + " в - " + vremia(), apehaBot_tme.chat_id)    
        time.sleep(random.randint(575, 595))

        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        link_work = apeha + src_1
        work_responce = session.get(link_work, headers=header).text

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print(src_3)
        print("Прошло 3700 - ")
        vremia()  
        apehaBot_tme.get_text_while("Прошло 3700 - " + src_3 + " в - " + vremia(), apehaBot_tme.chat_id)    
        time.sleep(random.randint(585, 595))


        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        link_work = apeha + src_1
        work_responce = session.get(link_work, headers=header).text

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print(src_3)
        print("Прошло 4200 - ")
        vremia()  
        apehaBot_tme.get_text_while("Прошло 4200 - " + src_3 + " в - " + vremia(), apehaBot_tme.chat_id)    
        time.sleep(random.randint(575, 595))



        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        link_work = apeha + src_1
        work_responce = session.get(link_work, headers=header).text

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print(src_3)
        print("выходим на новый круг")  
    vremia() 

    m += 1
    print("Круг" + str(m))
    time.sleep(random.randint(1, 2))
    apehaBot_tme.get_text_while("Круг - " + str(m) +" прошёл - " + src_3 + " в - " + vremia(), apehaBot_tme.chat_id)
print("Все сделали надо зайти проверить что не так " + str(m))
apehaBot_tme.get_text_while("Что то законччилось Ё!!!!!", apehaBot_tme.chat_id)
time.sleep(random.randint(1, 2))
apehaBot_tme.get_text_while("Что то законччилось Ё!!!!!", apehaBot_tme.chat_id)
time.sleep(random.randint(1, 2))
apehaBot_tme.get_text_while("Что то законччилось Ё!!!!!", apehaBot_tme.chat_id)
time.sleep(random.randint(1, 2))
apehaBot_tme.get_text_while("Что то законччилось Ё!!!!!", apehaBot_tme.chat_id)