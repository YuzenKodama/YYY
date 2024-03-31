from django.forms import ModelForm
from .models import PhotoPost

class PhotoPostForm(ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['category','tweet','comment',]