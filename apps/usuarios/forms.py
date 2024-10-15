
from .models import NewUser
from django.contrib.auth.forms import UserCreationForm


class FormUsers(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ('username','first_name','last_name','email','password1','password2')
        
    def __init__(self, *args, **kwargs):
        super(FormUsers, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None

