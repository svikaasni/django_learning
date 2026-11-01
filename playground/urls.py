from django.urls import path
from . import views 

#url configuration module
urlpatterns = [
    path('hello/',views.say_hello)# no need playground/hello only hello is enough because we have alrady included playground in the main urls.py file
]