from django import forms
from college.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class subscribeform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=subscribe
class contactform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=contact
class signupform(UserCreationForm):
    first_name= forms.CharField(
                          
                           widget= forms.TextInput(
                            attrs={
                                "class": "form-control",
                                'placeholder':'Enter your first name'}))
    last_name= forms.CharField(
                           widget= forms.TextInput(
                            attrs={
                            "class": "form-control",
                            'placeholder':'Enter last name'}))
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder':'Enter Username'
            }
        )
    )
    email=forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                'placeholder':'Enter Email'
            }
        )
    )
    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                'placeholder':'Enter Password'
            }
        )
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                'placeholder':'Confirmination Password'
            }
        )
    ) 
    class Meta:
        fields=('first_name','last_name','username', 'email','password1')
        model=User



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password1 = forms.CharField(max_length=63, widget=forms.PasswordInput)