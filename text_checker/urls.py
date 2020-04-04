from django.urls import path
from text_checker import views

urlpatterns = [path("", views.text_checker, name="index")]