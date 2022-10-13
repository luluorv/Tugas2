# Tugas 4

### Perbedaan antara asynchronous programming dengan synchronous programming
Asynchronous programming:
* Berupa multi-thread model (operasi atau program berjalan secara paralel)
* Non-blocking (mengirim beberapa request ke server)
* Operasi dapat dijalankan secara bersamaan tanpa menunggu operasi yang lain untuk selesai
* Lebih cepat

Synchronous programming:
* Berupa singe-thread model (satu operasi saja yang berjalan)
* Blocking (hanya dapat mengirim satu request ke server)
* Menunggu hingga request dijawab oleh server sebelum mengirim request lainnya 
* Lebih lambat

### Penerapan paradigma Event-Driven Programming 
Event-Driven Programming adalah paradigma programming dimana jalannya program ditentukan oleh event seperti action dari user, output sensor atau pesan dari program atau thread lain. Pada penambahan task, menggunakan AJAX POST untuk menyimpan title dan description dari task baru tersebut.

### Penerapan asynchronous programming pada AJAX
* Browser akan melakukan call JavaScript ke Ajax engine (membuat objek XMLHttpRequest)
* Di background, sebuah HTTP request dikirim ke server dan akan mendapatkan data yang sesuai
* Data HTML, XML atau JavaScript akan dikembalikan ke Ajax engine yang akan mengirim data yang direquest ke browser