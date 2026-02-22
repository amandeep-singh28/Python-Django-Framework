from django.urls import path
from . import views

# URL Configuration module
urlpatterns = [ # urlpatterns must stay as it is, because python looks for this only
    path('hello/', views.say_hello)
]