# Tugas 4
### [Link Aplikasi Heroku](https://katalogluluorv.herokuapp.com/todolist/)
Account: dummy, Hero

Password: pbp12345

### Kegunaan `{% csrf_token %}` pada elemen `<form>`
Untuk mencegah terjadinya serangan Cross-Site Request Forgery (CSRF). Serangan CSRF memaksa user yang melakukan autentikasi untuk mengeksekusi actions yang tidak diinginkan pada web application. `{% csrf_token %}` akan mengenerate token di server saat merender page dan akan mencross-check token ini untuk request yang masuk. Bila request tidak memiliki token, maka tidak akan dieksekusi. Bila tag ini tidak ada, maka kita tidak bisa mengidentifikasi dan mencompare source dan target origin. Dengan `{% csrf_token %}`, kita dapat memastikan bahwa request tersebut legitimate.

### Membuat elemen `<form>` secara manual
Kita dapat membuat `<form>` tanpa `{{ form.as_table }}` dengan membuat `<form>` pada `html` dengan method POST dan tambahkan juga tag `{% csrf_token %}`. Kemudian kita tinggal menambahkan tempat input dan juga button dengan type submit untuk mengirim data dari form tersebut.

### Proses alur data
Setelah user menekan button `new task`, dia akan diredirect ke halaman `todolist/create/` (`create_task.html`) dan juga memanggil fungsi `create_task`. Halaman `todolist/create/` adalah form dimana user dapat mengisi title dan description dari task. Setelah diisi dan menekan tombol submit, fungsi `create_task`akan mengecek apakah request methodnya POST atau tidak, bila iya, dia akan memetakan data dari form ke sebuah object task. Task tersebut kemudian akan di save, lalu menredirect user ke `todolist/` (`todolist.html`).

### Implementasi
* Membuat aplikasi baru `todolist` dengan menjalankan `python manage.py startapp todolist`
* Tambahkan path todolist pada `urls.py` dalam `project_django` dan `todolist`
* Membuat model pada `models.py` dengan atribut user, date, title, description
* Implementasi register, login, dan logout pada `views.py`, serta fungsi-fungsi lainnya. Untuk fungsi `show_todolist` tambahkan `@login_required(login_url='/todolist/login/')` agar hanya dapat diakses bila sudah login
* Tambahkan berkas `html` untuk `todolist` dan `create_task` lalu membuat routing untuk mengaksesnya serta fungsinya

### Bonus
* Pada `models.py` tambahkan atribut `is_finished`
* Membuat fungsi `change_status` dan `delete_task` pada views.py
* Dalam `todolist.html` buat if else statement untuk menyesuaikan teks dengan atribut `is_finished`. Tambahkan juga button `Change Status` untuk mengubah status dari task tersebut dan button `Delete Task` untuk menghapus sebuah task.
* Tambahkan path untuk `change_status` dan `delete_task` dalam urls.py

# Tugas 5
### Perbedaan dari Inline, Internal, dan External CSS
* Inline 
  - Menambahkan atribut `style` pada setiap tag HTML
  - Kelebihan:
    * Mudah menambahkan rule CSS ke dalam HTML
    * Tidak perlu membuat external style
  - Kekurangan:
    * Memakan banyak waktu untuk diimplmentasi
    * Dapat memengaruhi besar website dan download time
* Internal
  - Menambahkan tag `<style>` dalam `<head>` pada HTML
  - Kelebihan:
    * Dapat meggunakan class dan id selector 
    * Tidak perlu mengupload file lain karena hanya menambahkan kode pada HTML
  - Kekurangan:
    * Dapat menambah besarnya page dan loading time
* External
  - Menghubungkan HTML dengan file external `.css`
  - Kelebihan:
    * HTML lebih rapi dan terstruktur karena kode CSS ada pada file yang terpisah
    * File `.css` dapat digunakan berulang kali
  - Kekurangan:
    * Pages hanya akan terender dengan benar bila external CSS telah diload
    * Bila menghubungkan beberapa file CSS, download time dapat bertambah 

### Tag HTML5 
* `<!--...-->` : membuat comment
* `<a>` : membuat anchor
* `<article>` : membuat bagian konten dalam dokumen (artikel)
* `<body>` : membuat elemen body
* `<br>` : menambah line break
* `<button>` : membuat button
* `<div>` : membuat sebuah section dalam dokumen
* `<b>` : membuat text menjadi bold
* `<i>` : membuat text menjadi italic
* `<small>` : membuat text menjadi kecil
* `<big>` : membuat text menjadi besar
* `<form>` : membuat form
* `<head>` : memberi informasi mengenai dokumen
* `<header>` : membuat header
* `<footer>` : membuat footer
* `<html>` : membuat dokumen html
* `<input>` : membuat input field
* `<label>` : membuat label untuk form control
* `<li>` : membuat list item
* `<ol>` : membuat ordered list
* `<ul>` : membuat unordered list
* `<p>` : membuat paragraf
* `<code>` : menambahkan kode dalam bentuk text
* `<table>` : membuat tabel
* `<td>` : membuat cell tabel
* `<th>` : membuat header tabel
* `<tr>` : membuat row tabel
* `<textarea>` : membuat text area
* `<h1> - <h6>` : membuat heading 

### Tipe-tipe CSS selector
* `*` : memilih semua elemen pada halaman
* `#X` : memilih elemen berdasarkan id
* `.X` : memilih elemen berdasarkan class
* `X` : memilih elemen berdasarkan nama

### Implementasi
* Menambahkan stylesheet bootstrap pada `base.html`
* Menambahkan class dan stylenya dalam `style.css`
* Mengimplementasikan class dari `style.css` dan menambahkan atribut lain pada html

### Bonus
* Menambahkan class `.card:hover` untuk membuat efek pada cards
