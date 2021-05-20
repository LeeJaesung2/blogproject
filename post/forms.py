from django import forms
from .models import Blog

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body','image']
    # title = forms.CharField(max_length=200)
    # body = forms.CharField(widget=forms.Textarea)

    # def save(self, *args, **kwargs):
    #     super(CreatePostForm, self).save(*args, **kwargs)