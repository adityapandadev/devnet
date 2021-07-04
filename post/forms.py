from django import forms
from .models import Post
from django.forms import widgets

# Form for uploading feed posts content

class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('image','caption')
        widgets={
            'captions' : forms.TextInput(attrs = {'class':'form-control'}),
            'image':forms.FileInput(attrs = {'class':'form-control'}),

            }
        
