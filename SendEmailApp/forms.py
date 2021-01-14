from django import forms


# Custom Email Sending Form
class EmailForm(forms.Form):
    email = forms.CharField(max_length=100, widget=forms.TextInput())
    subject = forms.CharField(max_length=255, widget=forms.TextInput())
    message = forms.CharField(max_length=500, widget=forms.Textarea())