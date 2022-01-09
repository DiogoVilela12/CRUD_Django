from django.forms import ModelForm
from app.models import User


# Create the form class.
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'score']
