# Modul 10 - IP
#### Firda Utami Sukman - 103072400147 - IF-04-05



## 1. Apa itu IP Address?

IP Address (Internet Protocol Address) adalah alamat unik yang digunakan untuk mengidentifikasi perangkat pada jaringan komputer atau internet.

Contohnya:
- IPv4 : 192.168.1.1
- IPv6 : 2001:db8::1

IP Address berfungsi sebagai identitas perangkat di jaringan, menentukan alamat tujuan pengiriman data, dan mempermudah komunikasi antar perangkat dalam jaringan.


## 2. Traceroute dari suatu Website

Langkah - langkah melakukan traceroute:
- Buka Command Prompt
- Ketik website yang ingin dicek contoh tracert google.com
- Tekan enter
- Akan muncul daftar router/hop yang dilewati paket menuju website tujuan.

    Hasil traceroute menunjukkan bahwa paket data melewati beberapa router sebelum mencapai server tujuan Google dengan alamat IPv6: *2001:4860:4802:32::78*. Terdapat total sekitar 9 hop sebelum mencapai tujuan akhir. Dan pada hop ke-4 dan k-5 muncul pesan: *Request timed out*, Ini terjadi karena router pada hop tersebut tidak memberikan respon ICMP, namun paket tetap dapat melanjutkan perjalanan ke tujuan akhir.

## 3. Apa itu ICMP, MTU, dan TTL?
  a. ICMP (Internet Control Message Protocol)
     Merupakan protokol jaringan yang digunakan untuk mengirim pesan error dan informasi jaringan.

     Contoh penggunaannya adalah:
- **ping**
- **traceroute**