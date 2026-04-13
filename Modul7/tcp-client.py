# SOCKET = penjumlahan, pembagian, pengurangan, perkalian
from socket import * #import all

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(
    (serverName, serverPort)
)

print("[SYSTEM] Masukkan pesan")

running = True
while running:
    # input
    message = input("> ")

    # mengirim ke server
    # encode = adbdhfb = 1010101010100
    clientSocket.send(message.encode())

    # kalo exit = socket ditutup
    # Exit, exIT, EXIT
    if message.lower == "exit":
        print("[SYSTEM] keluar dari progran")
        running = False
        break

    # menerima pesan dari server
    modifiedMessage = clientSocket.recv(2048)

    print("[SERVER] pesan : ", modifiedMessage.decode())

# menutup socket yang tidak dipakai
clientSocket.close()
print("[SYSTEM] socket ditutup")