from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={
                'id': 'photoUpload',
                'class': 'd-none',
                'accept': 'image/*'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'width:100%; height:180px; font-size:16px; padding:12px;',
                'placeholder': 'Write your tweet here...'
            }),
        }
        
class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class  Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')