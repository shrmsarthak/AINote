from django.forms import ModelForm
from manager.models import Patient


class RegisterForm(ModelForm):
username = forms.CharField(max_length=100)
password = forms.CharField(widget=PasswordInput)

    class Meta:
        model = ModelForm
        fields = ["username", "password"]