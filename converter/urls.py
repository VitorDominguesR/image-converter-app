from django.urls import path
from . import views

urlpatterns = [
    path('', views.convert_jpeg_to_png, name='convert_image'),
]