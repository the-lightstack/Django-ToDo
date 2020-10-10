from django import forms


class Add_Task_Form(forms.Form):
    task_name=forms.CharField(label="",max_length=300)

#class Delete_Button(forms.Form):