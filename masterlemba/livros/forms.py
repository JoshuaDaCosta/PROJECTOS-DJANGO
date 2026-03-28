from django import forms
from .models import Livros  # importa o teu modelo


class LivroForm(forms.ModelForm):
    data_pub = forms.DateField(
        input_formats=["%d/%m/%Y", "%Y-%m-%d"],
        widget=forms.DateInput(attrs={"placeholder": "dd/mm/aaaa"}),
    )

    class Meta:
        model = Livros
        fields = "__all__"
        verbose_name = "Livro"  # nome singular
        verbose_name_plural = "Livros"  # nome plural correto
