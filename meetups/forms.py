from django import forms
#from .models import Participants

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Participants
#         fields = ['email']

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Enter email Id')