from django import forms
from django.core.exceptions import ObjectDoesNotExist

class URLForm(forms.Form):
    url = forms.URLField(
        label='チェックするページのURL',
        max_length=200,
        required=True,
    )