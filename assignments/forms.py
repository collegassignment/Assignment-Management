from django import forms
from assignments.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm

class assignmentform(forms.ModelForm):
    class Meta:
        model=assignment
        fields='__all__'

class newform(forms.ModelForm):
    class Meta:
        model=new
        fields='__all__'

class profileform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=studentprofile
class loginform(UserCreationForm):
    class Meta:
        fields='__all__'
        model=User
class uploadsform(forms.ModelForm):
    class Meta:
        model=uploads
        fields='__all__'
class PasswordChangeForm(PasswordChangeForm):
    oldpassword=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                'placeholder':'Enter Email'
                
            }
        )
    )
    Newpassword1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                'placeholder':'Enter Password'
            }
        )
    )
    Newpassword2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                'placeholder':'Confirmination Password'
            }
        )
    ) 
    class Meta:
        fields=('oldpassword','Newpassword1','Newpassword2')
        model=User
