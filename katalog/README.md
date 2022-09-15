# Tugas 2
### Link [Aplikasi Heroku](https://katalogluluorv.herokuapp.com/)

#### 1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`
![image](https://user-images.githubusercontent.com/103396686/190281876-384a3b10-61e6-46e6-9c27-4f0e5fa7945e.png)

Saat kita membuat request pada web aplikasi berbasis Django, request tersebut akan dibawa ke urls (`urls.py`). Urls akan mengecek request tersebut dan memanggil views (`views.py`) kemudian views akan membuat koneksi antara template (`html`) dan model (`models.py`). Dalam sebuah aplikasi web, kita memerlukan tiga hal: data, layout dan logic. Setiap hal tersebut akan dihandle secara terpisah agar lebih mudah diimplementasi (seperation of concern). Models berperan dalam mendapatkan data dari database yang dapat dihubungkan dengan model logic. Data yang didapatkan oleh models tersebut kemudian akan diberikan pada template yang akan merender data-data tersebut. Views adalah tempat app logic berada. Penetapan data yang digunakan template dan koneksinya pada model akan dilakukan oleh views. Setelah views selesai, berkas html akan dikirimkan kembali ke user dan ditampilkan pada browsernya.


#### 2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment berperan dalam mengatasi terjadinya konflik dependencies. Konflik ini terjadi apabila ada lebih dari satu proyek django dan satu proyek menggunakan versi yang berbeda dengan yang lain. Agar kita tidak perlu install dan uninstall django ke versi yang sesuai dengan versi yang digunakan untuk satu proyek, kita dapat menggunakan virtual environment sehingga dependencies hanya akan diinstall pada environment tersebut.

Penggunaan virtual environment bukan sesuatu yang wajib, namun penggunaannya adalah best practice untuk menghindari error dari perbedaan versi django yang terinstall dan versi django yang digunakan oleh proyek django tertentu.


#### 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
* Pada `views.py`, membuat fungsi `show_katalog` dengan data katalog berupa `CatalogItem`. Dari situ `katalog.html` akan dirender.
* Dalam folder `katalog` import `path` dari `django.url` dan `show_katalog` dari `katalog.views`, lalu menambahkan urlpattern dengan path menggunakan `show_katalog`. Pada `url.py` dalam folder `project_django` juga tambahkan routing untuk mengakses url katalog.
* Melakukan migrasi skema model ke dalam database menggunakan `makemigrations`, `migrate`, dan `loaddata`. Menambahkan isi pada `katalog.html` agar sesuai dengan data yang akan ditampilkan.
* Setelah selesai, `add`, `commit`, dan `push` perubahan yang telah dilakukan. Pada settings repositori bagian secrets, tambahkan nama aplikasi dan API key. Tunggu hingga deployment berhasil pada github, lalu aplikasi Heroku tersebut sudah dapat diakses.
