from django.contrib import admin
from django.urls import path
from app.views import home, product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('product/', product),
]
