# Laprak-Jarkom Week 2
## Modul 3 - HTTP

### Basic HTTP GET/Response Interaction
Langkah pertama yang dilakukan adalah memastikan cache browser sudah dikosongkan, kemudian menjalankan Wireshark dan mengaktifkan filter `http` pada kolom Display Filter. Setelah itu, Wireshark mulai menangkap paket.

Copy dan paste link berikut di browser:
http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html

<img width="1167" height="300" alt="Image" src="https://github.com/user-attachments/assets/32639401-2244-4e79-a2da-bd767d5f62b1" />

Browser menampilkan halaman sederhana berisi pesan konfirmasi bahwa file berhasil diunduh.

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/a8dbcb2c-613e-41b4-917f-53448df2d35d" />
Dari hasil capture Wireshark dengan filter `http`, terlihat dua paket utama yang tertangkap. Paket pertama adalah pesan **HTTP GET** yang berisi permintaan untuk mengambil file `HTTP-wireshark-file1.html`. Paket kedua adalah respons dari server berupa **HTTP/1.1 200 OK**, yang menandakan bahwa server berhasil memproses permintaan dan mengirimkan kembali isi file HTML. Terdapat konten yang dikirim bertipe `text/html`.

---

###  HTTP Conditional GET/Response Interaction
Setelah itu cache browser dikosongkan terlebih dahulu lalu wireshark dijalankan dan URL berikut diakses sebanyak **dua kali** secara berurutan:
http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/feb5dd7b-4286-4ebc-8eff-3b11b6083b97" />

Browser menampilkan halaman berisi informasi bahwa file ini memiliki tanggal modifikasi yang tidak akan berubah.

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/9b39117e-dd73-4abd-a037-d32bc7d052b4" />

Pada akses **pertama**, browser akan mengirimkan HTTP GET  tanpa header `If-Modified-Since`. Server merespons dengan **HTTP/1.1 200 OK** dan mengirimkan isi file secara lengkap, sekaligus menyertakan header `Last-Modified` yang berisi informasi kapan file terakhir dimodifikasi.

Pada akses **kedua**, browser secara otomatis menyertakan header `If-Modified-Since` yang berisi tanggal dari respons sebelumnya. Karena file tidak mengalami perubahan sejak permintaan pertama, server hanya merespons dengan **HTTP/1.1 304 Not Modified** tanpa mengirimkan body file sama sekali. Browser kemudian menggunakan salinan file yang tersimpan di cache lokal. Mekanisme ini disebut **Conditional GET**

---

### Retrieving Long Documents
Langkah selanjutnya adalah mengamati bagaimana HTTP menangani pengiriman dokumen yang berukuran besar. Link berikut dapat diakses melalui browser:
http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/a4e55a6f-8987-4cab-a4ef-498f1f3644dc" />

Browser akan menampilkan dokumen Bill of Rights Amerika Serikat yang lumayan panjang.

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/792e05b1-1c52-4782-816a-42381a47a7e5" />

Terlihat bahwa respons dari server tidak langsung datang dalam satu paket. Hal ini karena ukuran file HTML-nya cukup besar sehingga tidak muat dikirim sekaligus dalam satu paket TCP. Seperti mengirim paket barang yang terlalu besar maka barangnya dipecah jadi beberapa kotak kecil dulu, dikirim satu per satu, baru di tujuan disusun lagi jadi satu. Sama seperti file HTML yang dipecah menjadi 4 potongan (segmen TCP) yang dikirim secara berurutan. Wireshark menandai hal ini dengan label [TCP segment of a reassembled PDU] di setiap potongannya.
Setelah semua potongan tiba, Wireshark menyusunnya kembali menjadi satu pesan HTTP yang utuh. Inilah cara kerja TCP — memastikan semua data sampai dengan lengkap dan berurutan meskipun harus dipecah-pecah terlebih dahulu.

---

### HTML Documents dengan Embedded Objects
Untuk mengamati bagaimana browser menangani halaman web yang memuat objek dari server berbeda, Link berikut dapat diakses melalui browser:
http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/e2b3952e-7c38-4efd-a02a-7d9dd60c62a7" />

Browser akan menampilkan halaman HTML sederhana yang memuat dua gambar, yaitu logo Pearson dan cover buku Computer Networking edisi ke-8.

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/f8f737b9-d24a-40b7-9432-19312fe6fec3" />

Terlihat bahwa untuk membuka satu halaman web ini, browser ternyata mengirimkan beberapa HTTP GET sekaligus. Ini karena cara kerja browser — pertama ia mengunduh file HTML utamanya dulu dari gaia.cs.umass.edu. Setelah file HTML itu dibaca, browser baru "sadar" bahwa di dalam halaman tersebut ada dua gambar yang perlu diambil juga. Maka browser otomatis mengirimkan permintaan tambahan untuk mengunduh masing-masing gambar. Salah satu gambar yaitu cover buku tidak disimpan di server yang sama. Jadi browser harus "pergi ke dua tempat berbeda" hanya untuk menampilkan satu halaman web. Ini menunjukkan bahwa membuka satu halaman web bisa memicu banyak HTTP request ke beberapa server sekaligus, tergantung dari mana saja objek-objek di dalam halaman itu disimpan.

---

### HTTP Authentication
Langkah terakhir adalah mengamati mekanisme autentikasi HTTP. Link berikut dapat diakses di browser dan memerlukan login:
http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/27a8c0ba-d9fb-4892-a6f9-17cfc6128be7" />

Browser menampilkan dialog pop-up autentikasi yang meminta username dan password sebelum halaman dapat diakses.

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/d8fc11d0-ee29-44c7-a87f-9b2039e39568" />

Setelah memasukkan credentials yang benar, halaman berhasil ditampilkan dengan pesan konfirmasi bahwa halaman bersifat password protected dan berhasil diunduh.

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/6e044d2b-a7d4-4931-8e7f-e071b88b20a8" />

Terlihat bahwa proses login HTTP terjadi dalam dua tahap. Pada tahap pertama, browser mencoba membuka halaman seperti biasa tanpa membawa username dan password sama sekali. Server kemudian menolak permintaan tersebut dengan mengirimkan respons HTTP/1.1 401 Unauthorized yang artinya kita belum punya izin untuk mengakses halaman ini. Di dalam respons penolakan itu, server juga menyertakan pesan bahwa halaman ini membutuhkan login terlebih dahulu sebelum bisa dibuka.

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/3b9e759c-6c88-4a95-b678-40ac2a466068" />

Pada tahap kedua, setelah pengguna memasukkan username dan password, browser akan mengirim ulang permintaan dengan membawa informasi login yang sudah diubah. Server memverifikasi dan merespons HTTP/1.1 200 OK: halaman berhasil dibuka.



