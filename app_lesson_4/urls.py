from django.http import HttpResponse
from .views import index
from django.urls import path


urlpatterns = [
    path('lesson_4', index),
]