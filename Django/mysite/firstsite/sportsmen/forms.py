from django import forms
from .models import *

class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Sportsman
        fields = ['title', 'slug', 'content', 'is_published', 'sport']