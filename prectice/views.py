from django.views.generic import ListView
from Album.models import Album

class HomeView(ListView):
    model = Album
    template_name = 'index.html'
    context_object_name = 'data'
