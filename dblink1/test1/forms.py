from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User1


class User1CreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User1
        fields = ('email', )


class User1ChangeForm(UserChangeForm):

    class Meta:
        model = User1
        fields = ('email', )
