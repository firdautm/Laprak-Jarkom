# Modul 5 - UDP
UDP (User Datagram Protocol) adalah cara mengirim data di jaringan yang fokus pada kecepatan, yaitu data langsung dikirim tanpa mengecek apakah data sudah sampai atau belum. Jadi, pengirim tidak menunggu balasan dari penerima, sehingga prosesnya lebih cepat tapi tidak menjamin data diterima dengan lengkap atau urut. Karena itu, UDP biasanya dipakai untuk hal yang butuh kirim data cepat seperti streaming, game online, atau panggilan suara di internet.

## Tugas
### Langkah - langkah:
1. mengunduh file trace penangkapan paket UDP yang telah disediakan dengan link http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip


2. Kemudian ekstrak file dengan nama http-ethereal-trace-5 dan buka filenya dengan wireshark
   <img width="1920" height="1080" alt="Screenshot (84)" src="https://github.com/user-attachments/assets/5ea9eb18-5bda-44f8-97c1-2f710f609857" />


3. Tampilan setelah dibuka dengan wireshark
   <img width="1920" height="1080" alt="Screenshot (101)" src="https://github.com/user-attachments/assets/77871c4a-b9c8-409b-beab-d16b0dfa5f6b" />

---

#### Pertanyaan
- Pilih satu paket UDP yang terdapat pada trace Anda. Dari paket tersebut, berapa banyak 
“field” yang terdapat pada header UDP? Sebutkan nama-nama field yang Anda temukan!

  <img width="1920" height="1080" alt="Screenshot (102)" src="https://github.com/user-attachments/assets/d22a9296-06c3-4d2f-9201-211b9d30c75f" />

  Dari paket UDP pada trace Wireshark, header UDP memiliki 4 field, yaitu Source Port, Destination Port, Length, dan Checksum.



- Perhatikan informasi **"content field"** pada paket yang Anda pilih di pertanyaan 1. Berapa panjang (dalam satuan byte) masing-masing field yang terdapat pada header UDP?


  Pada header UDP, setiap field memiliki panjang tetap (*fixed size*). Berdasarkan informasi content field pada paket UDP di Wireshark, panjang masing-masing field adalah:
  - **Source Port** : 2 byte  
  - **Destination Port** : 2 byte  
  - **Length** : 2 byte  
  - **Checksum** : 2 byte
  
- Nilai yang tertera pada ”Length” menyatakan nilai apa? Verfikasi jawaban Anda melalui 
paket UDP pada trace. 
  <img width="748" height="307" alt="Screenshot (102) copy" src="https://github.com/user-attachments/assets/09fcb291-1a2d-4fb8-91eb-1cb1dc54d425" />
  Nilai pada field **Length** menyatakan panjang total paket UDP, yaitu header UDP dan data (payload).

  Pada trace Wireshark:
  Header UDP = 8 byte  
  Payload = 50 byte  
  Length = 58 byte
  
  Sehingga:
  Length = 8 byte + 50 byte = 58 byte.

- Berapa jumlah maksimum byte yang dapat disertakan dalam payload UDP?
  Jumlah maksimum byte yang dapat disertakan dalam payload UDP adalah **65.507 byte**.

  Hal ini karena ukuran maksimum UDP adalah 65.535 byte, sedangkan header UDP berukuran 8 byte dan header IP berukuran 20 byte.
  
  Sehingga:
  65.535 − 8 − 20 = 65.507 byte.

- Berapa nomor port terbesar yang dapat menjadi port sumber?

  
  Nomor port terbesar yang dapat menjadi port sumber adalah **65535**. Hal ini karena field nomor port pada header UDP memiliki ukuran 16 bit. Dengan ukuran tersebut, nilai port yang dapat digunakan berada pada rentang 0 hingga 65535 (2¹⁶ − 1), sehingga 65535 merupakan nilai maksimum yang dapat digunakan sebagai source port.

- Berapa nomor protokol untuk UDP? Berikan jawaban Anda dalam notasi heksadesimal dan 
desimal. Untuk menjawab pertanyaan ini, Anda harus melihat ke bagian ”Protocol” pada 
datagram IP yang mengandung segmen UDP.

  Nomor protokol untuk UDP adalah:

  Desimal : 17  
  Heksadesimal : 0x11

- Periksa pasangan paket UDP di mana host Anda mengirimkan paket UDP pertama dan paket 
UDP kedua merupakan balasan dari paket UDP yang pertama. (Petunjuk: agar paket kedua merupakan balasan dari paket pertama, pengirim paket pertama harus menjadi tujuan dari 
paket kedua). Jelaskan hubungan antara nomor port pada kedua paket tersebut!

  <img width="1168" height="723" alt="Screenshot 2026-04-05 134251" src="https://github.com/user-attachments/assets/98f1cb16-998e-4789-9906-62c36edc3996" />
  <img width="1039" height="720" alt="Screenshot 2026-04-05 134235" src="https://github.com/user-attachments/assets/428b1b89-4c0c-4a9f-80ab-cf44299c20c5" />

  Pada pasangan paket UDP, nomor port pada paket balasan saling bertukar dengan paket sebelumnya. Source port pada paket pertama menjadi destination port pada paket balasan, dan destination port pada paket pertama menjadi source port pada paket balasan.

  Paket pertama : Src Port 4334 → Dst Port 161  
  Paket balasan : Src Port 161 → Dst Port 4334

  

