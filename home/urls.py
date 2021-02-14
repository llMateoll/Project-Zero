from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('' , views.home , name='home') ,
    path('index/' , views.Test , name='index') ,  

]