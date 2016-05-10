from django import forms
from django.forms import SelectDateWidget

from pagedown.widgets import PagedownWidget

from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.CharField(widget=SelectDateWidget)

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish"
        ]