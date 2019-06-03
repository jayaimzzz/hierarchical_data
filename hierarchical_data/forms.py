from django import forms
from mptt.forms import TreeNodeChoiceField

from hierarchical_data.models import File

class AddFileForm(forms.Form):
    name = forms.CharField(max_length=50)
    parent = TreeNodeChoiceField(queryset=File.objects.all())