TCP Client
Berfungsi untuk mengirim pesan ke server dan menerima balasan dari server.

```python
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
```
- Membuat socket TCP
- connect() digunakan untuk menghubungkan client ke server

```python
print("[SYSTEM] Masukkan pesan")
running = True
while running:
```
Digunakan untuk menampilkan pesan dan membuat loop agar client bisa kirim pesan berkali-kali.

```python
message = input("> ")
```
Digunakan untuk menerima input dari user.

```python
clientSocket.send(message.encode())
```
Digunakan untuk mengirim pesan ke server dalam bentuk bytes.

```python
if message.lower() == "exit":
```
Digunakan untuk mengecek apakah user ingin keluar.

```python
print("[SYSTEM] keluar dari progran")
running = False
break
```
Jika user mengetik "exit", maka program akan berhenti.

```python
modifiedMessage = clientSocket.recv(2048)
print("[SERVER] pesan : ", modifiedMessage.decode())
```
Digunakan untuk menerima balasan dari server dan menampilkannya.

```python
clientSocket.close()
print("[SYSTEM] socket ditutup")
```
Digunakan untuk menutup koneksi.


