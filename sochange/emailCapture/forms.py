from django import forms

class EmailCaptureForm(forms.Form):
    email = forms.EmailField()
