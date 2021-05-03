from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    title = forms.CharField(label="Title",max_length=50)
    details = forms.CharField(label="Description",widget=forms.Textarea)
    date_due = forms.DateTimeField(label="Due Date",required=False)
    priority = forms.IntegerField(label="Priority")
    class Meta:
        model=Task
        fields = ['title','details','date_due','priority']