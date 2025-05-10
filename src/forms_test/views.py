
from django.shortcuts import render

from .forms import LoginModelForm, ProductModelForm, TestForm
from .models import Product

def home(request):
    form = LoginModelForm(request.POST or None)
    if form.is_valid():
        usuario = form.cleaned_data.get('usuario')
        correo = form.cleaned_data.get('correo')
        password = form.cleaned_data.get('password')
        print(usuario, correo, password)
        form.save()
    return render(request, "forms.html", {"form": form})