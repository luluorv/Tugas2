# Tugas 3
### [Link Aplikasi Heroku](https://katalogluluorv.herokuapp.com/todolist/)
dummy account: dummy, Hero
password: pbp12345

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
* Implementasi register, login, dan logout pada `views.py`, serta fungsi-fungsi lainnya. Untuk fungsi `show_todolist` tambahkan `@login_required(login_url='/todolist/login/')` agar hnaya dapat diakses bila sudah login
* Tambahkan berkas `html` untuk `todolist` dan `create_task` lalu membuat routing untuk mengaksesnya serta fungsinya

### Bonus
* Pada `models.py` tambahkan atribut `is_finished`
* Membuat fungsi `change_status` dan `delete_task` pada views.py
* Dalam `todolist.html` buat if else statement untuk menyesuaikan teks dengan atribut `is_finished`. Tambahkan juga button `Change Status` untuk mengubah status dari task tersebut dan button `Delete Task` untuk menghapus sebuah task.
* Tambahkan path untuk `change_status` dan `delete_task` dalam urls.py
