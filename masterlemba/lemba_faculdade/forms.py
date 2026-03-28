from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "conteudo"]  # troca pelos campos que tens no teu modelo
