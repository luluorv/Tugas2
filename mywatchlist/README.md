# Tugas 3
### Link Aplikasi Heroku [HTML](https://katalogluluorv.herokuapp.com/mywatchlist/html/), [XML](https://katalogluluorv.herokuapp.com/mywatchlist/xml/), [JSON](https://katalogluluorv.herokuapp.com/mywatchlist/json/)

### Perbedaan antara JSON, XML, dan HTML
* HTML (Hyper Text Markup Language):
  - Untuk membuat web pages dan web application
  - Sebuah markup language
  - Dapat membuat static pages
  - Digunakan untuk menampilkan data, bukan mentrasport data
  - Mendefinisikan hubungan antara web pages
  - Markup language digunakan untuk mendefinisikan text document dalam tag yang mendefinisikan web page

* XML (eXtensible Markup Language):
  - Untuk membuat web pages dan web application
  - Mentransport data dan tidak menampilkan data
  - Mengutamakan kesederhanaan, keumuman dan kegunaan di internet
  - Sebuah format data tekstual melalui Unicode untuk bahasa yang beragam
  - Didesain untuk dokumen, namun juga digunakan untuk representasi dara struktur seperti pada web service

* JSON (JavaScript Object Notation):
  - Berupa format data-interchange ringan 
  - Tidak bergantung pada bahasa
  - Berbasis bahasa pemograman JavaScript
  - Mudah untuk dimengerti

### Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery ini diperlukan dalam pengembangan platform pada saat kita perlu mengirimkan data dari satu stack ke stack lainnya. Data tersebut dapat berupa HTML, XML dan JSON.

### Implementasi checklist
1. Membuat aplikasi `mywatchlist` dengan 
```shell
python manage.py startapp mywatchlist
```
dan menambahkan `mywatchlist` pada `NSTALLED APPS` dalam `project_django`
```shell
INSTALLED_APPS = [
    ...,
    'mywatchlist'
]
```

2. Menambahkan path mywatchlist dalam `urls.py` pada `project_django` di variabel `urlpatterns`
```shell
...
path('mywatchlist/', include('mywatchlist.urls')),
...
```

3. Membuat models `MyWatchList` dengan menambahkan kode berikut ke `models.py`
```shell
from django.db import models

class WatchlistItem(models.Model):
    watched = models.BooleanField() 
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.TextField()
```

4. Menambahkan data `MyWatchList` dengan membuat berkas `initial_mywatchlist_data.json` dalam folder `fixtures` dengan isi minimal 10 data, lalu lakukan migrasi
```shell
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_mywatchlist_data.json
```
5. Mengimplementasikan penampilan data dalam format HTML, XML dan JSON dengan menambahkan kode berikut pada `views.py`
``` shell
from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

def show_html(request):
    watchlistitem = WatchlistItem.objects.all()
    context = {
    'list_watchlist': watchlistitem,
    'nama': 'Clarissa Thea Aryanto',
    'id': '2106634673'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Lalu membuat file `mywatchlist.html` pada folder `templates`
```shell
{% extends 'base.html' %}

 {% block content %}

  <h1>Tugas 3 Assignment PBP/PBD</h1>

  <h5>Name: </h5>
  <p>{{nama}}</p>

  <h5>Student ID: </h5>
  <p>{{id}}</p>

  <table>
    <tr>
      <th>Watched?</th>
      <th>Title</th>
      <th>Rating</th>
      <th>Release Date</th>
      <th>Review</th>
    </tr>
    
    {% for things in list_watchlist %}
        <tr>
            {% if things.watched %} <td>Watched</td> {% else %} <td>Haven't watched</td> {% endif %}
            <td>{{things.title}}</td>
            <td>{{things.rating}}</td>
            <td>{{things.release_date}}</td>
            <td>{{things.review}}</th>
        </tr>
    {% endfor %}  
  </table>

 {% endblock content %}
```

6. Membuat routing URL data di atas
```shell
from django.urls import path
from mywatchlist.views import show_html, show_xml, show_json

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]
```

7. Melakukan deploy ke Heroku dan menambahkan kode berikut pada `Procfile`
```shell
release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json && python manage.py loaddata initial_mywatchlist_data.json'
```

8. Postman
* HTML
![image](https://user-images.githubusercontent.com/103396686/191658882-8a4dbcde-f692-485e-aae8-8e569aef38ae.png)

* XML
![image](https://user-images.githubusercontent.com/103396686/191658912-420726a7-fc8f-4cb8-8482-aafbea6e57e7.png)

* JSON
![image](https://user-images.githubusercontent.com/103396686/191658941-3f27c842-2ca4-49b3-b323-88374a9bf700.png)


9. Menambahkan unit test pada `test.py`
```shell
from django.test import TestCase, Client

class WatchListTest(TestCase):
    def test_html(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    
    def test_xml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_json(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
```

### Bonus
Untuk mendapatkan jumlah yang sudah ditonton dan yang belum, pada `views.py` tambahkan 
```shell
watchlistitem = WatchlistItem.objects.all()
watched = WatchlistItem.objects.filter(watched = True).count()
not_watched = WatchlistItem.objects.filter(watched = False).count()
count = watched >= not_watched
```
dan dalam `context` buat variabel `watched_a_lot` untuk menyimpan data count
```shell
    context = {
    ...
    'watched_a_lot': count
    ...
    }
```
Dalam berkas `mywatchlist.html`, tambahkan if else statement untuk menampilkan pesan yang sesuai
```shell
  {% if watched_a_lot %} <h3>Selamat, kamu sudah banyak menonton!</h3>
  {% else %} <h3>Wah, kamu masih sedikit menonton!</h3> {% endif %}
```


