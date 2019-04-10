from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, CharField
from .models import User1
from test2.models import *


class User1CreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User1
        fields = ('email', )


class User1ChangeForm(UserChangeForm):

    class Meta:
        model = User1
        fields = ('email', )


class SearchObject2(ModelForm):

    name = CharField(required=False)

    class Meta:
        model = Object2
        fields = ('name',)

        widgets = {'name': TextInput(attrs={'placeholder': 'Name'}, ), }
