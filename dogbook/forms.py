from django import forms
from dogbook.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["name", "imagefile"]
