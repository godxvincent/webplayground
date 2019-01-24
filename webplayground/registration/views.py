from .forms import UserCreationFormWithEmail, ProfileForm
from django.views.generic import CreateView, UpdateView
from .models import Profile
from django.urls import reverse_lazy
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?registration'

    def get_form(self, form=None):
        new_form = super(SignUpView, self).get_form()
        # Los nombres de los campos hay que sacarlos de los nombres que genera automaticamente
        # Django, por tanto toca entrar en el codigo generado visto a través del navegador

        new_form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        new_form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Dirección de correo'})
        new_form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
        new_form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Repite contraseña'})
        return new_form


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
