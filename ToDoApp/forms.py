from django import forms


class Add_Task_Form(forms.Form):
    task_name=forms.CharField(label="task_name",max_length=300)