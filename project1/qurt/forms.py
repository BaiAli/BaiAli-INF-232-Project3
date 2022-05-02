from tkinter import Widget
from django.forms import ModelForm
from .models import Facts

class TraditionForm(ModelForm):

    class Meta():
         model = Facts
         fields = ['conclusion',]