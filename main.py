import imghdr
import os
import smtplib
from email.message import EmailMessage




def menu(user,password):
    print("\nMAİL ATMA UYGULAMASINA HOŞ GELDİNİZ...")

    #Kişi Listesi Çıkarma
    contacts = open("mails.txt","r")
    person = contacts.readline()
    contact_list = [person]
    #Listede Hala Birisi Varsa Okumaya Devam Eder
    while person:
        person = contacts.readline()
        contact_list.append(person)

    msg_Contact = contact_list
    msg_Title = ""
    msg_Text = ""
    msg_File\
        = []
    while True:
        giris = int(input("\nSeçim Yapınız : \n1)Başlık Ekle\n2)Metin Ekle\n3)Dosya Ekle\n4)Maili Görüntüle\n5)Maili Gönder\n"))

        #Başlık Ekleme/Değiştirme
        if giris == 1:
            if msg_Title == "":
                msg_Title = input("Başlık Giriniz :")
            else:
                msg_Title = input("Başlığı Değiştiriniz :")
        #Metin Ekleme/Değiştirme
        elif giris == 2:
            if msg_Text =="":
                msg_Text = input("Metin Giriniz :")
            else:
                msg_Text = input("Metini Değiştiriniz :")

        #Dosya Ekleme
        elif giris == 3 :
            msg_File.append(input("Dosya Adını Giriniz :\n#DOSYANIN AYNI KLASÖRDE OLMASINA DİKKAT EDİNİZ\n"))

        #Mail Görüntüleme
        elif giris == 4:
            print(f"Başlık : {msg_Title}\nMetin : {msg_Text}\nDosya : {msg_File}")
        #Maili Gönderme
        elif giris == 5:
            mesajAtma(user,password,msg_Title,msg_Text,msg_File,msg_Contact)
        #Hata
        else:
            print("Hatalı Giriş Tekrar Deneyiniz\n")


def mesajAtma(usr,pw,baslik,metin,dosya,list):

    e_Mesaj = EmailMessage()


    #Başlık
    e_Mesaj["Subject"] = baslik
    #İçeriğin işlenmesi
    e_Mesaj.set_content(metin)

    for dosyalar in dosya:
        with open(dosyalar,"rb")as f:
            dosya_data = f.read()
            dosya_name = f.name
            dosya_type = imghdr.what(f.name)
        e_Mesaj.add_attachment(dosya_data,maintype="image",subtype=dosya_type,filename=dosya_name)


    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp :
        smtp.login(usr,pw)
        for kisi in list:
            smtp.send_message(e_Mesaj,usr,kisi)
if __name__=="__main__":
    giris = False
    if giris==False:
        giris_user = input("E-postanızı Giriniz : ")
        giris_password = input("Uygulama Şifrenizi Giriniz : ")
        giris = True
    if giris:
        try:
            menu(giris_user,giris_password)
        except:
            print("E-postalar Gönderildi.....")