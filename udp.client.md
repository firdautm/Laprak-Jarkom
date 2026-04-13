## UDP Client
Berfungsi untuk mengirim pesan ke server tanpa koneksi dan menerima balasan.

```python
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(5)
```
- Membuat socket UDP
- Memberi batas waktu 5 detik untuk menunggu balasan

```python
message = input('Masukkan kalimat lowercase : ')
```
Digunakan untuk menerima input dari user.

```python
clientSocket.sendto(message.encode(), (serverName, serverPort))
```
Digunakan untuk mengirim pesan ke server.

```python
if message.lower() == 'exit':
```
Jika user ingin mematikan server.

```python
elif message.lower() == 'keluar':
```
Jika user hanya ingin keluar dari client.

```python
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
```
Digunakan untuk menerima balasan dari server.

```python
except timeout:
```
Digunakan untuk menangani jika server tidak merespons.

```python
clientSocket.close()
```
Digunakan untuk menutup koneksi.