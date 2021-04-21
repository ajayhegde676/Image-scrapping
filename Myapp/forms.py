from django import forms
from Myapp.models import user


class Newuser(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'


