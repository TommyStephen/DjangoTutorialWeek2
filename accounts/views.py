from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'