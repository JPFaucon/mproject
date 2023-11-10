from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    # first_name = forms.CharField(label="First name", max_length=100)
    # last_name = forms.CharField(lavel='Last name', max_length=100)
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee']


    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['assignee'].required = False