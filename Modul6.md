# Modul 6 - TCP 

## 6.1 Pengantar
Modul ini mempelajari protokol TCP secara mendetail dengan menganalisis jejak (trace) segmen TCP saat mengirim file 150 KB dari komputer ke server jarak jauh. Pembahasan meliputi penggunaan sequence number dan acknowledgement untuk memastikan pengiriman data yang andal, mekanisme congestion control untuk mencegah kemacetan jaringan, serta flow control yang diatur oleh penerima. Selain itu, modul juga membahas proses pembentukan koneksi TCP dan menganalisis performa koneksi seperti throughput dan round-trip time (RTT).


## 6.2 Menangkap Tansfer TCP dalam Jumlah Besar dari Komputer Pribadi ke Remote Server  
   1. Download file alice.txt


      Download file dari http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html
      <img width="1920" height="1080" alt="Screenshot (105)" src="https://github.com/user-attachments/assets/de6d00cf-485d-462f-aa63-fe504957e64b" />
  
   2. Buka halaman upload


      Buka http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html
      <img width="1920" height="1080" alt="Screenshot (106)" src="https://github.com/user-attachments/assets/8e172a24-33d5-40b0-a44b-27177cbbaae3" />

  
   3. Buka Wireshark, pilih interface Wi-Fi, mulai capture paket


      <img width="1920" height="1080" alt="Screenshot (108)" src="https://github.com/user-attachments/assets/9275bafb-9906-4227-8105-6a4144bdfd9e" />

   
   4. Pilih file alice.txt pada halaman upload, lalu klik "Upload alice.txt file"


      <img width="1920" height="1080" alt="Screenshot (107)" src="https://github.com/user-attachments/assets/d0ab12b3-5bc1-4cae-b79b-1a03b3e541ac" />

  
   5. Setelah muncul halaman Congratulations, hentikan capture Wireshark
      <img width="1920" height="1080" alt="Screenshot (109)" src="https://github.com/user-attachments/assets/6396a8d1-f320-45fe-b117-fa2fff41a676" />


   6. Filter paket dengan filter tcp pada Wireshark


      Terlihat paket TCP dan beberapa HTTP. File diupload dipecah menjadi segmen-segmen kecil melalui mekanisme SYN.


      <img width="1920" height="1080" alt="Screenshot (110)" src="https://github.com/user-attachments/assets/2a5c3bfa-edbf-48e0-9591-60109b2369bb" />


   7. Paket HTTP/1.1 200 OK menandakan file berhasil diterima server
      <img width="1920" height="1080" alt="Screenshot (111)" src="https://github.com/user-attachments/assets/7bef94ed-046b-4cc7-a0ef-ea9ad23c08cb" />


## 6.3 Tampilan Awal pada Captured Trace 
   Ekstrak file wireshark-traces.zip dari http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip lalu buka file tcp-ethereal-trace-1 dengan Wireshark.  
   
   
   <img width="1920" height="1080" alt="Screenshot (130)" src="https://github.com/user-attachments/assets/35ef056b-d97a-4d20-ae40-0343e837c2c3" />


   ### Pertanyaan
   1. Berapa alamat IP dan nomor port TCP yang digunakan oleh komputer klien (sumber) untuk 
      mentransfer file ke gaia.cs.umass.edu?


      IP klien adalah 10.218.15.227 dan port TCP yang digunakan adalah port 5814. Hal ini terlihat pada detail paket HTTP yang ter-highlight, di mana bagian TCP menunjukkan Src Port: 5814.


      <img width="1320" height="435" alt="Screenshot (111) copy" src="https://github.com/user-attachments/assets/5953354c-e277-464c-8e0b-8cb7b64f9527" />



   2. Apa alamat IP dari gaia.cs.umass.edu? Pada nomor port berapa ia mengirim dan menerima segmen TCP untuk koneksi ini?


      Alamat IP gaia.cs.umass.edu adalah 128.119.245.12. Server menggunakan port 80 untuk mengirim dan menerima segmen TCP pada koneksi ini (HTTP standard port).

      <img width="1920" height="1080" alt="Screenshot (111)" src="https://github.com/user-attachments/assets/fd6facdb-45de-4924-8893-e0361cca4496" />


   3. Berapa alamat IP dan nomor port TCP yang digunakan oleh komputer klien Anda (sumber) untuk mentransfer  ke gaia.cs.umass.edu?
      IP klien: 10.218.15.227, port TCP: 58154. Koneksi menggunakan protokol HTTP (port 80 pada server) untuk mentransfer file alice.txt ke gaia.cs.umass.edu.


## Dasar TCP 


   ### Pertanyaan
   1. Berapa nomor urut segmen TCP SYN yang digunakan untuk memulai sambungan TCP antara komputer klien dan gaia.cs.umass.edu? Apa yang dimiliki segmen tersebut sehingga teridentifikasi sebagai segmen SYN? 


      <img width="1920" height="1080" alt="Screenshot (132)" src="https://github.com/user-attachments/assets/90fed97c-7ef0-44fd-9fcf-86fd05425a38" />


      IP klien: 192.168.1.102, port: 1161 → server 128.119.245.12 port 80. Filter tcp.flags.syn == 1 && tcp.flags.ack == 0 menunjukkan paket SYN pertama Seq=0 Win=16384 Len=0 MSS=1460 SACK_PERM.


   2. Berapa nomor urut segmen SYNACK yang dikirim oleh gaia.cs.umass.edu ke komputer klien sebagai balasan dari SYN? Berapa nilai dari field Acknowledgement pada segmen SYNACK? Bagaimana gaia.cs.umass.edu menentukan nilai tersebut? Apa yang dimiliki oleh segmen  sehingga teridentifikasi sebagai segmen SYNACK?


      <img width="1920" height="1080" alt="Screenshot (133)" src="https://github.com/user-attachments/assets/f231b7ed-0ea8-4bd7-87e3-4407f230e47a" />


      segmen SYN-ACK yang dikirim oleh gaia.cs.umass.edu memiliki Sequence Number = 0 dan Acknowledgement = 1. Nilai acknowledgement tersebut ditentukan dari sequence number milik klien yang ditambah 1, sebagai tanda bahwa server telah menerima segmen SYN dari klien. Segmen ini dapat diidentifikasi sebagai SYN-ACK karena pada bagian informasi paket terdapat flag SYN dan ACK yang aktif secara bersamaan ([SYN, ACK]).


   3. Berapa nomor urut segmen TCP yang berisi perintah HTTP POST?


      <img width="1920" height="1080" alt="Screenshot (136)" src="https://github.com/user-attachments/assets/a022a7c2-e598-4902-81c9-960f1f71f5f1" />


      Nomor urut segmen TCP yang berisi perintah HTTP POST adalah: 199


   4. Berapa RTT dari setiap segmen TCP?


      <img width="1920" height="1080" alt="Screenshot (123)" src="https://github.com/user-attachments/assets/a253aa50-86fe-43c6-bede-d3bb9a087ae3" />


      Dari grafik RTT (Statistics > TCP Stream Graphs > Round Trip Time), RTT berkisar antara ~50 ms hingga ~270 ms. Pola zigzag yang konsisten menunjukkan variasi RTT akibat mekanisme slow start dan congestion avoidance TCP.


   5. Berapa total ukuran data yang ditransmisikan?


      <img width="1920" height="1080" alt="Screenshot (124)" src="https://github.com/user-attachments/assets/90349393-acbd-4c01-a69b-a05cc632f5f6" />


      Dari detail reassembled TCP segments, terdapat 122 segmen dengan total 164.090 bytes (~164 KB). Sebagian besar frame membawa payload 1460 bytes (MSS), kecuali beberapa segmen terakhir.
      

   6. Berapa ukuran receive window (rwnd) pada segmen SYN-ACK? Apa artinya?


      <img width="1920" height="1080" alt="Screenshot (125)" src="https://github.com/user-attachments/assets/b55aa65e-3941-4a8c-a148-b2cb1decefb4" />


      Pada segmen SYN-ACK (No. 2), ukuran window adalah 5840 bytes (Calculated window size: 5840).


   7. Apakah ada retransmisi pada trace ini?


      <img width="1920" height="1080" alt="Screenshot (126)" src="https://github.com/user-attachments/assets/6ca654cd-bea3-44f2-bf76-35bfb6002fc1" />


      Tidak ada retransmisi. Filter tcp.analysis.retransmission menghasilkan 0 paket (Displayed: 0), yang berarti tidak terjadi retransmisi selama sesi TCP ini berlangsung.


   8.  Tampilkan segmen TCP dengan filter ACK dari server


       <img width="1920" height="1080" alt="Screenshot (127)" src="https://github.com/user-attachments/assets/98c50e5d-2985-4ed6-8780-48fffeab35f8" />


       Filter tcp.port == 1161 && tcp.flags.ack == 1 menunjukkan server (128.119.245.12) mengirimkan ACK secara berkala. 


   9. Berapa throughput rata-rata koneksi TCP ini?


      <img width="1920" height="1080" alt="Screenshot (128)" src="https://github.com/user-attachments/assets/240b4509-0291-4e34-a671-e4470e08d32a" />


      Dari grafik Throughput (Statistics > TCP Stream Graphs > Throughput), throughput rata-rata berkisar antara 200–270 Kbps. Grafik relatif stabil dengan sedikit variasi akibat congestion control.


## 6.5 Congestion Control pada TCP 
### Pertanyaan
1. Pada bagian mana algoritma ”congestion avoidance” mengambil alih?
   Tidak terlihat congestion avoidance yang signifikan. Tidak ditemukan paket retransmisi maupun penurunan window size yang drastis, sehingga TCP tidak masuk ke fase congestion avoidance selama transfer berlangsung.


2. Analisis grafik Sequence Numbers (Stevens) menggunakan file alice.txt


   <img width="1920" height="1080" alt="Screenshot (129)" src="https://github.com/user-attachments/assets/c6a693c5-1046-4394-9b80-5254bda4f06c" />


   Grafik Sequence Numbers (Stevens) menunjukkan peningkatan linear yang konsisten dari 0 bytes hingga ~160 KB selama 5 detik pengiriman. Tidak ada penurunan tajam (drop) pada sequence number, mengkonfirmasi tidak adanya packet loss selama transmisi.






































