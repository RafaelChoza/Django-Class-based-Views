from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Product(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f"/products/products/{self.slug}"
    
    def get_edit_url(self):
        return f"/products/my-products/{self.slug}"
    
    def get_delete_url(self):
        return f"/products/my-products/{self. slug}/delete"

class DigitalProduct(Product):
    class Meta:
        proxy = True