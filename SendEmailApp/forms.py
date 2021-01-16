from django import forms

from multi_email_field.forms import MultiEmailField     # Multiple recipient email addresses


# Custom Email Sending Form
class EmailForm(forms.Form):
    DESIGNATION_CHOICES = [
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Lawyer', 'Lawyer'),
        ('Business', 'Business'),
    ]

    fullname = forms.CharField(label='Your Name', max_length=50, widget=forms.TextInput())
    company = forms.CharField(label='Company Name', max_length=50, required=False, widget=forms.TextInput())
    designation = forms.ChoiceField(required=False, choices = DESIGNATION_CHOICES)
    email_input = forms.EmailField(label="Input Email", required=False, max_length=60, widget=forms.TextInput())
    # email = forms.CharField(label='Recipient', max_length=100, widget=forms.TextInput())
    email = MultiEmailField(label='Recipient')
    subject = forms.CharField(max_length=255, widget=forms.TextInput())
    message = forms.CharField(max_length=500, widget=forms.Textarea())
    attachment = forms.FileField(label='', required=False, widget=forms.ClearableFileInput(attrs={ 'multiple':True }))

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        #Email-input
        self.fields['email_input'].widget.attrs['id'] = 'email_input'
        self.fields['email_input'].widget.attrs['onkeypress'] = 'eventListener(event)'
        self.fields['email_input'].widget.attrs['onkeyup'] = 'eventListener2(event)'

        # MultiEmailField
        self.fields['email'].widget.attrs['readonly'] = 'readonly'

        # message
        self.fields['message'].widget.attrs['placeholder'] = 'Write something.....'


        # File-attachment
        self.fields['attachment'].widget.attrs['style'] = 'background-color: red;'      # not displaying the main file-upload btn, hide it on-page
        self.fields['attachment'].widget.attrs['id'] = 'upfile'
        self.fields['attachment'].widget.attrs['onchange'] = 'sub(this)'

        # NB: With this method, can add PLACEHOLDER to the form fields.

    