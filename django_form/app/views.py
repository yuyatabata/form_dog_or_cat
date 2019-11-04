from django import forms
from django.shortcuts import render
from .models import User

def index(request):
    return redirect('app:diag_1)

def get_diag_1():
    if form.is_valid():
        form.save()
        return render('app:finish')
    else:
        return render
