from django import forms


class AdditionForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
