from django import forms


# Custom Email Sending Form
class EmailForm(forms.Form):
    DESIGNATION_CHOICES = [
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
    ('Lawyer', 'Lawyer'),
    ('Business', 'Business'),
]

    fullname = forms.CharField(label='Your Name', max_length=50, widget=forms.TextInput())
    company = forms.CharField(label='Company Name', max_length=50, widget=forms.TextInput())
    designation = forms.ChoiceField(choices = DESIGNATION_CHOICES) 
    email = forms.CharField(label='Recipient', max_length=100, widget=forms.TextInput())
    subject = forms.CharField(max_length=255, widget=forms.TextInput())
    message = forms.CharField(max_length=500, widget=forms.Textarea())
    attachment = forms.FileField(label='', required=False, widget=forms.ClearableFileInput(attrs={ 'multiple':True }))