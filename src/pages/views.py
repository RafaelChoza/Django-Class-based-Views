import os

from django import get_version
from django.conf import settings
from django.shortcuts import render


def home(request):
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version() + "PROBANDO CAMBIOS",
        "python_ver": os.environ["PYTHON_VERSION"] + "MAS CAMBIOS",
    }

    return render(request, "pages/home.html", context)
