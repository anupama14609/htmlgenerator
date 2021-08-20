from django import forms
from .models import HtmlGenerator
from ckeditor.widgets import CKEditorWidget

class HtmlGeneratorForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(),label="Text Editor")
    class Meta:
        model=HtmlGenerator
        fields=('body',)