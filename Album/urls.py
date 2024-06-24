from django.urls import path
from .views import AlbumCreateView, AlbumUpdateView, AlbumDeleteView, CustomLoginView, CustomLogoutView,RegistrationView,ProfileUpdateView
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('', AlbumCreateView.as_view(), name='add_album'),
    path('edit/<int:pk>/', AlbumUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', AlbumDeleteView.as_view(), name='delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    
]