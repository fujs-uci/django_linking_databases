from django.forms import ModelForm, TextInput
from .models import *


class Object2CreationForm(ModelForm):

    class Meta:
        model = Object2
        fields = ('name', 'type', )

        widgets = {'name': TextInput(attrs={'placeholder': 'Name'}, ),
                   'type': TextInput(attrs={'placeholder': 'Type'}, ), }
