from django import forms


class AddStudentForm(forms.Form):
    username = forms.CharField(label="Student Username", max_length=150)


