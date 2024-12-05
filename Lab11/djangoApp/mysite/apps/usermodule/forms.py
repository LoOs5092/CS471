from django import forms
from django_recaptcha.fields import ReCaptchaField
from django.contrib.auth.models import User

class RecoverForm(forms.Form):
    email = forms.EmailField()

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        # Ensure passwords match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()
    captcha_field=ReCaptchaField() # import recaptha field
