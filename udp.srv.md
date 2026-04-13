UDP Server
Berfungsi menerima pesan dari client tanpa koneksi, lalu mengirim balasan.

```python
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
```
- Membuat socket UDP
- bind() untuk menghubungkan ke port tertentu

```python
message, clientAddress = serverSocket.recvfrom(2048)
```
Digunakan untuk menerima pesan sekaligus alamat client.

```python
original_message = message.decode().strip()
```
Digunakan untuk mengubah pesan menjadi string.

```python
if original_message.lower() == 'exit':
```
Jika client mengirim "exit", server akan berhenti.

```python
modifiedMessage = original_message.upper()
```
Pesan diubah menjadi huruf besar.

```python
serverSocket.sendto(modifiedMessage.encode(), clientAddress)
```
Digunakan untuk mengirim balasan ke client.

```python
serverSocket.close()
```
Digunakan untuk menutup server.