from django import forms
from magazine.models import Reporter
class Form(forms.ModelForm):
    class Meta:
        model = Reporter
        fields = ("__all__")

