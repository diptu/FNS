from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Format: YYYY-MM-DD')
    email      = forms.EmailField(help_text='A valid email address, please.')
    contact    = forms.CharField(help_text='Provide a valid contact information')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', 'contact','email','gender')
