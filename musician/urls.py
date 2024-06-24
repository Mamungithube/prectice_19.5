from django.contrib import admin
from django.urls import path,include
from .views import MusicianCreateView
urlpatterns = [
    path('', MusicianCreateView.as_view(), name='add_musician'),
    
]