from socket import fromshare
from django import forms
from todolist.models import Task

class CreateTask(forms.Form):
    title = forms.TextInput()
    description = forms.Textarea()