from django import forms
from .models import Volunteer

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'age', 'gender', 'text']