from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Requerido, 254 carácteres com máximo y debe ser válido")

    class Meta:
        # Es importante resaltar que usar el campo email es posible porque hace parte del modelo de username
        # Pero indicar un campo que no existe en el modelo user es imposible.
        model = User
        fields = ('username',  'email', 'password1', 'password2')
        # Es posible que aqui se sobre escriba el campo widget pero al hacerlo reemplazamos todas las validaciones
        # heredadas del UserCreationForm
