# TODO: Implement Routings Here

from django.urls import path
from todolist.views import register, login_user, logout_user, show_todolist, create_task, change_status, delete_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create/', create_task, name='create_task'),
    path('status/<int:id>', change_status, name='change_status'),
    path('delete/<int:id>', delete_task, name='delete_task'),
]