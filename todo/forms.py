from django import forms
from .models import Todos, Lists


class TodosForm(forms.ModelForm):

    class Meta:
        model = Todos
        fields = ('proj_desc', 'when')


class ListsForm(forms.ModelForm):

    class Meta:
        model = Lists
        fields = ('name', 'comment', 'message',)
