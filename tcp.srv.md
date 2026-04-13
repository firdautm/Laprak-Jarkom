TCP Server
Berfungsi menerima koneksi dari client, memproses pesan, lalu mengirim balasan.

```python
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
```

- bind() digunakan untuk menghubungkan socket ke port tertentu
- '' berarti menerima koneksi dari semua IP 

```python
serverSocket.listen(1)
```
Artinya server mulai “mendengarkan” koneksi masuk. Angka 1 berarti maksimal 1 koneksi dalam antrian.

```python
connectionSocket, addr = serverSocket.accept()
```
Saat client terhubung, server membuat connection socket baru khusus untuk client tersebut.

```python
message = connectionSocket.recv(2048).decode()
```
Ini digunakan untuk menerima data

Jika client disconnect, maka:
```python
if not message:
    break
```

```python
if message.lower() == "exit":
```
Jika client mengirim "exit", server akan berhenti.


```python
print("[SYSTEM] client ingin keluar")
running = False
break
```
```python
modifiedMessage = message.upper()
print("[SERVER] diterima: ", modifiedMessage)
```
Pesan akan diubah menjadi huruf besar lalu ditampilkan di server.

```python
connectionSocket.send(modifiedMessage.encode())
```
Digunakan untuk mengirim kembali pesan ke client.

```python
connectionSocket.close()
serverSocket.close()
```
Digunakan untuk menutup koneksi dengan client dan server.