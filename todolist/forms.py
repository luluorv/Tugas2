from socket import fromshare
from django import forms

class CreateTask(forms.Form):
    title = forms.TextInput()
    description = forms.Textarea()