from django.urls import path
from .views import publicnewshome


app_name = 'PublicNews'

urlpatterns = [
    
    path('home/', publicnewshome, name='PublicNewsHome'),
]