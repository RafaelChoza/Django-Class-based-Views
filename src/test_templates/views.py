from django.shortcuts import render

from datetime import datetime

from django.contrib import messages

def test_view(request):
    my_list = ["Mouse", "Laptop", "Teclado", "Audifonos", "Multicontactos", "Celular"]
    context = {
        "view_title": "MI TITULO INCREÍBLE",
        "my_number": 675,
        "my_number2": 2000,
        "today": datetime.now().today(),
        "my_list": my_list,
    }
    template = "test_templates/detail-view.html"

    messages.add_message(request, messages.INFO, 'Mensaje de prueba 1')
    messages.add_message(request, messages.INFO, 'Mensaje de prueba 2')
    return render(request, template, context)