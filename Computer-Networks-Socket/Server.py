
import socket

host = '127.0.0.1'
port = 12345
buffer_boyut=2048

def broadcast(mesaj, sender_socket):
    for uye in bagli_uyeler:
        if uye != sender_socket:
            uye.send(mesaj.encode())

def server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host,port))
    server_socket.listen(1)
    print('Sunucu dinlemede...')

    while True:
        client_socket, client_address = server_socket.accept()
        print('Bağlantı gerçekleşti', client_address)

        # Kullanıcı adını iste
        client_socket.send("Kullanıcı adınızı giriniz: ".encode())
        kullanici_adi = client_socket.recv(buffer_boyut).decode()
        print('Kullanıcı adı:', kullanici_adi)

        # Diğer istemcilere kullanıcının bağlandığını bildir
        message = print(kullanici_adi,"sohbete katıldı!")
        broadcast(message, client_socket)

        # Kullanıcı mesajını göster
        client_socket.send("Mesajınızı girin".encode())
        gelen_mesaj = client_socket.recv(buffer_boyut).decode()
        print(kullanici_adi,':',gelen_mesaj)

        client_socket.close()

bagli_uyeler = []
server()
