
import socket

buffer_boyut=2048
host = '127.0.0.1'
port = 12345

def broadcast(mesaj, sender_socket):
    for uye in bagli_uyeler:
        if uye != sender_socket:
            uye.send(mesaj.encode())
def client():

    isimler = []
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host,port))

    # Sunucudan mesaj al
    mesaj = client_socket.recv(buffer_boyut).decode()
    print('Sunucu mesajı:',mesaj)

    # Kullanıcı adını gir
    kullanici_adi = input('')
    client_socket.send(kullanici_adi.encode())
    for i in range(len(isimler)):
        if i in isimler:
            print("Bu ada sahip kullanıcı vardır litfen başka bir isim giriniz!!")
            break
        else:
            isimler+=[i]

    print("Hoşgeldiniz",kullanici_adi)
    cikis=print("Çıkış yapmak için x tuşunu basınız")

    # Mesaj yaz
    while True:
        mesaj=input("Mesajınızı girin:")
        client_socket.send(mesaj.encode())

        if mesaj=="x":
            mesaj = print(kullanici_adi, "sohbetten ayrıldı!")

        client_socket.close()

bagli_uyeler = []
client()