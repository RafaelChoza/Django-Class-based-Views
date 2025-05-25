from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, RedirectView

from products.views import(
    ProductListView, 
    ProductDetailView, 
    DigitalProductListView, 
    ProductRedirectIdView, 
    ProductRedirectView,
    ProtectedProductDetailView,
    ProtectedProductCreateView,
    ProtectedProductUpdateView,
    ProtectedProductDeleteView,
    ProductApiListView
    )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about-us/", RedirectView.as_view(url = "/products/about/")),
    path("about/", TemplateView.as_view(template_name = "products/about.html")),
    path("team/", TemplateView.as_view(template_name = "products/team.html")),
    path("products/", ProductListView.as_view(template_name = "products/product_list.html")),
    path("products-api/", ProductApiListView.as_view()),
    path("products/<int:pk>", ProductDetailView.as_view(template_name = "products/product_detail.html")),
    path("digital-products/", DigitalProductListView.as_view(template_name = "products/product_list.html")),
    path("products/<slug:slug>/", ProductDetailView.as_view()),
    path("p/<int:pk>/", ProductRedirectIdView.as_view()),
    path("p/<slug:slug>/", ProductRedirectView.as_view()),

    #path("my-products/<slug:slug>/", ProtectedProductDetailView.as_view()),
    path("my-products/create/", ProtectedProductCreateView.as_view()),
    path("my-products/<slug:slug>/", ProtectedProductUpdateView.as_view()),
    path("my-products/<slug:slug>/delete/", ProtectedProductDeleteView.as_view()),
    path("my-products/", ProductListView.as_view(template_name = "products/product_list.html")),
]