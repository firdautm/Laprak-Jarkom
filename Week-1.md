# Laprak-Jarkom Week 1
Firda Utami Sukman - 103072400147 - IF-04-05


## Modul 1 - RUNNING MODUL
### Instalasi Tools
Langkah pertama yang dilakukan adalah mengunduh aplikasi Wireshark melalui situs resminya yaitu https://www.wireshark.org
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8187d2d2-28f1-4cec-b615-11d689cc3520" />
<br>
Download sesuai perangkat yang digunakan.



<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7e710bb8-2277-4890-a52c-2e3e890704a3" />

Setelah berhasil diunduh, langkah selanjutnya adalah menjalankan file tersebut untuk memulai proses instalasi hingga proses instalasi selesai dan aplikasi berhasil terpasang pada laptop.


<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/652cf4a8-a28d-4d1c-8cfb-0399ccaad3c2" />

Tampilan awal Wireshark akan menampilkan daftar interface jaringan yang tersedia pada perangkat, seperti Wi-Fi atau Ethernet.

## Modul 2 - PENGENALAN TOOLS
### Fungsi Tools
#### Membuka Interface dan Memulai Capture
<img width="1920" height="1080" alt="Screenshot (15)" src="https://github.com/user-attachments/assets/f7321d7e-734c-471e-b4bf-65c46f19be0c" />


Pilih salah satu interface jaringan yang tersedia, misalnya Wi-Fi, kemudian menekan tombol Start Capture untuk mulai menangkap paket data yang melewati jaringan tersebut. Wireshark akan mulai menampilkan lalu lintas data yang terjadi pada jaringan secara langsung.


![WhatsApp Image 2026-03-08 at 6 01 55 PM](https://github.com/user-attachments/assets/7c0e223e-c634-42f7-8353-268c14af9bf8)
##### 1. Packet List Pane
Packet List Pane merupakan bagian yang menampilkan daftar seluruh paket jaringan yang berhasil ditangkap selama proses capture berlangsung.

##### 2. Packet Details Pane
Packet Details Pane menampilkan rincian informasi dari paket yang dipilih pada Packet List Pane. Informasi paket ditampilkan dalam bentuk struktur protokol berlapis, seperti Frame, Ethernet, dan protokol jaringan lainnya

##### 3. Packet Bytes Pane
Packet Bytes Pane menampilkan isi paket dalam bentuk kode hexadecimal dan ASCII. Data ini merupakan representasi data mentah dari paket yang dikirim melalui jaringan.

### Penggunaan Display Filter
Untuk memudahkan proses analisis paket, Wireshark menyediakan fitur Display Filter yang berada pada kolom berwarna hijau di bagian atas. Fitur ini memungkinkan untuk menyaring paket sehingga hanya paket dengan kriteria tertentu saja yang ditampilkan.
Contohnya, buka browser dan akses halaman web menggunakan protokol HTTP pada link berikut:
http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html

<img width="882" height="212" alt="Screenshot (16)" src="https://github.com/user-attachments/assets/6c71440f-52b7-4ad4-8386-76beae755cb5" />


Setelah halaman tersebut dimuat, kembali ke Wireshark lalu masukkan kata http pada kolom Display Filter. Setelah filter diterapkan, akan menampilkan hanya paket-paket yang berkaitan dengan protokol HTTP.

<img width="1920" height="561" alt="Screenshot (17)" src="https://github.com/user-attachments/assets/81461c6e-1a7d-4fd2-b143-53e1214d8733" />

Dengan ini otomatis akan lebih mudah mengidentifikasi paket HTTP yang dihasilkan dari aktivitas membuka halaman web pada browser tanpa harus melihat seluruh paket



<img width="1920" height="1080" alt="Screenshot (21)" src="https://github.com/user-attachments/assets/2f9e786a-676a-4148-b19f-a0520b833b8f" />


Pada salah satu paket HTTP terlihat pesan HTTP/1.1 200 OK yang merupakan respon dari server yang menandakan bahwa permintaan halaman web dari browser telah berhasil diproses oleh server.
Kode status 200 OK menunjukkan bahwa server berhasil menerima permintaan dan mengirimkan kembali data halaman web yang diminta oleh pengguna.
