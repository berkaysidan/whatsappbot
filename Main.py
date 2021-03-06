
import os
import pandas as pd
import time
import pyautogui as pt
from time import sleep
from pandas.io.parsers import read_csv
import pyperclip

data = pd.DataFrame(
    read_csv("Numaralar.csv")  # csv dosyasını kendiniz için doldurunuz.
)

isim = data["İsim"]
tel_numbers = data["Tel Numarası"]
mesaj = str(input("Göndermek istediğiniz mesajı yazınız: "))
baslamadanonce = str(input("Whatsapp'ı karanlık modda mı kullanıyorsunuz?(E/H):")).upper()    
saat = int(input("Göndermek istediğiniz saat dilimini giriniz(xx): "))
dakika = int(input("Göndermek istediğiniz dakika dilimini giriniz(xx): "))

def zaman(time_hour: int, time_min: int, wait_time: int = 5,
          ) -> None:

    global sleep_time
    
    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Hatalı Zaman Formatı")
    else:
        os.system("C:\\Users\\xxxx\\AppData\\Local\\WhatsApp\\WhatsApp.exe") # Default olarak whatsapp'ın bilgisayarınızdaki kurulu olduğu dizini gireceğiniz alan xxxx'e kullanıcı adınızı giriniz.

    if time_hour == 0:
        time_hour = 24
    call_sec = (time_hour * 3600) + (time_min * 60)

    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec

    if current_hour == 0:
        current_hour = 24

    current_to_second = (current_hour * 3600) + \
        (current_minute * 60) + current_second
    left_time = call_sec - current_to_second

    if left_time <= 0:
        left_time = 86400 + left_time

    sleep_time = left_time - wait_time
    print(f"Whatsapp açıldı ve {sleep_time} saniye sonra yollanacaktır.")

    time.sleep(sleep_time)

    time.sleep(2)

    time.sleep(wait_time - 2)


# örneği zaman(13, 54) -----> Göndermek istediğiniz Zamanı girin
zaman(saat, dakika)
for i in range(len(data)):  # buradaki range kısmına  csv dosyasındaki kişi sayısı kadar değer giriliyor.
    if baslamadanonce == "E":
            numara = pt.locateOnScreen("numaragiris.png", confidence=.6)
            x = numara[0]
            y = numara[1]
    
        # Numara Arama
            def noara():
                global x, y
                positionara = pt.locateOnScreen("numaragiris.png", confidence=.6)
                x = positionara[0]
                y = positionara[1]
                pt.moveTo(x, y, duration=.5)
                pt.moveTo(x, y+90, duration=.5)
                pt.tripleClick() 
                pt.write(str(tel_numbers[i]))

            noara()
            sleep(5)
            #Numarayı Bulduktan sonra o numaradaki kişiye tıklama

            def kisitikla():
                global x, y
                kisibul = pt.locateOnScreen("numaragiris.png", confidence=.6)
                x = kisibul[0]
                y = kisibul[1]
                pt.moveTo(x-100, y+250, duration=.5)
                pt.click()
            kisitikla()
            sleep(3)
        # Numara Arama
        # Mesaj girme kısmına tıklama
            msggiris = pt.locateOnScreen("smiley_paperclip.png", confidence=.6)
            x = msggiris[0]
            y = msggiris[1]

        # Mesajı gönderme

            def getmessage():

                global x, y
                position = pt.locateOnScreen("smiley_paperclip.png", confidence=.6)
                x = position[0]
                y = position[1]
                pt.moveTo(x, y, duration=.5)
                pt.moveTo(x+200, y+20, duration=.5)
                pt.click()
                pyperclip.copy(
                    f"Merhaba {isim[i]}, {mesaj}")
                pt.hotkey("ctrl", "v")
                pt.hotkey("enter")
            getmessage()
            
    else:
        numara_2 = pt.locateOnScreen("numaragiris2.png", confidence=.6)
        x = numara_2[0]
        y = numara_2[1]

        def noara2(): #burada whatsapp'ın karanlık veya aydınlık moduna göre belirlenmesine yarayan fonksiyon bulunur.
            global x, y
            positionara = pt.locateOnScreen("numaragiris2.png", confidence=.6)
            x = positionara[0]
            y = positionara[1]
            pt.moveTo(x, y, duration=.5)
            pt.moveTo(x, y+90, duration=.5)
            pt.tripleClick()
            pt.write(str(tel_numbers[i]))

        noara2()
        sleep(5)
        def person_check_1():
            global x, y
            kisibul = pt.locateOnScreen("numaragiris2.png", confidence=.6)
            x = kisibul[0]
            y = kisibul[1]
            pt.moveTo(x-100, y+250, duration=.5)
            pt.click()

        person_check_1()
        sleep(3)
        msggiris_1 = pt.locateOnScreen("smiley_paperclip2.png", confidence=.6)
        x = msggiris_1[0]
        y = msggiris_1[1]

        def getmessage_1():
            global x, y
            position = pt.locateOnScreen("smiley_paperclip2.png", confidence=.6)
            x = position[0]
            y = position[1]
            pt.moveTo(x, y, duration=.5)
            pt.moveTo(x+200, y+20, duration=.5)
            pt.click()
            pyperclip.copy(
                f"Merhaba {isim[i]}, {mesaj}")
            pt.hotkey("ctrl", "v")
            pt.hotkey("enter")
        getmessage_1()
print(f"Mesajlarınız dosyada belirtilen {int(len(data))} kişiye yollanmıştır.")       



    

    


        




    


