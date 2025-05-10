from django import forms

from .models import Product, Usuario

YEARS = [x for x in range(1978, 2030)]

MY_CHOICES = [
    ("db_value1", "Opción 1"),
    ("db_value2", "Opción 2"),
    ("db_value3", "Opción 3"),
]

class LoginModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["usuario", "correo", "password"]
        labels = {
            "usuario": "Usuario",
            "correo": "Correo",
            "password": "Password"
        }
        widgets = {
            "password": forms.PasswordInput()
        }

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password and len(password) <= 7:
            raise forms.ValidationError("El password debe tener 8 o más caracteres")
        return password


class ProductModelForm(forms.ModelForm):
    labels = {
        "title": "Mi etiqueta para el título",
        "slug": "Mi etiqueta para el slug",
        "price": "Mi etiqueta para el precio",
    }
    class Meta:
        model = Product
        fields = [
            "title",
            "slug",
            "price"
        ]
        exclude = []

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if len(title) <= 10:
            raise forms.ValidationError("El título debe tener al menos 10 caracteres")
        return title
    
    def clean_slug(self, *args, **kwargs):
        slug = self.cleaned_data.get("slug")
        if len(slug) <= 10:
            raise forms.ValidationError("El slug debe tener al menos 10 caracteres")
        if "supermarca" not in slug:
            raise forms.ValidationError("El slug debe contener la palabra 'supermarca'")
        return slug
    
    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise forms.ValidationError("El precio no puede ser menor a 0")
        return price
    

class TestForm(forms.Form):
    fecha = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    some_text = forms.CharField(label="Ingresa un Texto", initial="Texto inicial", widget=forms.Textarea(attrs={"rows": 4, "cols": 50}))
    boolean = forms.BooleanField(initial=True)
    integer = forms.IntegerField(initial=60)
    email = forms.EmailField(initial="correo@ejemplo")
    opciones = forms.CharField(label="Selecciona una opción", widget=forms.Select(choices=MY_CHOICES))
    opciones_radio = forms.CharField(label="Selecciona una opción", widget=forms.RadioSelect(choices=MY_CHOICES))
    opciones_checkbox = forms.CharField(label="Selecciona una opción", widget=forms.CheckboxSelectMultiple(choices=MY_CHOICES))

    def clean_integer(self, *args, **kwargs):
        integer = self.cleaned_data.get("integer")
        if integer > 100:
            raise forms.ValidationError("La calificación no puede ser mayor a 100")
        return integer
    
    def clean_some_text(self, *args, **kwargs):
        some_text = self.cleaned_data.get("some_text")
        if len(some_text) < 10:
            raise forms.ValidationError("El texto debe tener al menos 10 caracteres")
        return some_text