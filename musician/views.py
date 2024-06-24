from django.views.generic.edit import CreateView
from .forms import musicianForm
from .models import musician  # Ensure to import the Musician model if it's used directly

class MusicianCreateView(CreateView):
    model = musician
    form_class = musicianForm
    template_name = 'musician_form.html'
    success_url = '/'  # Redirect to home page or another relevant page after success

    def form_valid(self, form):
        # Custom form processing can be done here
        return super().form_valid(form)
