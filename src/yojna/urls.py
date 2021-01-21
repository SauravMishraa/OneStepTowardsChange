from django.urls import path
from .views import yojnahome
app_name = 'Yojna'

urlpatterns = [
    
    path('home/', yojnahome, name='YojnaHome'),
]