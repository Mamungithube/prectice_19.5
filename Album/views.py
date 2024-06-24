from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy
from .models import Album
from .forms import Albumform
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import RegistrationForm, UserUpdateForm
from .models import Profile
class AlbumCreateView(CreateView):
    model = Album
    form_class = Albumform
    template_name = 'album_form.html'
    success_url = reverse_lazy('home')

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = Albumform
    template_name = 'album_form.html'
    success_url = reverse_lazy('home')

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'album_confirm_delete.html'
    success_url = reverse_lazy('home')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'
    success_url = reverse_lazy('home')

class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        valid = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return valid

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = UserUpdateForm
    template_name = 'profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.profile
