from django import forms
from .models import Todo, List


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('proj_desc', 'when')


class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('name', 'comment', 'message',)
