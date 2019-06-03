from django import forms

class AddFileForm(forms.Form):
    body = forms.CharField(max_length=50)