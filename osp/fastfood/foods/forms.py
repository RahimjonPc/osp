from django import forms
from django.forms import Textarea
from foodslogic.models import Comments
from foods.models import Foods
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields[field].widget = Textarea(attrs={'rows':5})