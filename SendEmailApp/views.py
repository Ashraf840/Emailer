from django.shortcuts import render
from .forms import EmailForm
from django.contrib import messages


# Account Activation HTML Templated Email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template import Context

# Speeding up Django Email Sending using Multithreading
import threading


# Multi-threading
class EmailThread(threading.Thread):
    def __init__(self, msg):
        self.email = msg
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()



# Create your views here.
def home(request):
    context = {
        'title':'Home'
    }
    return render(request, 'SendEmailApp/index.html', context)


def sendEmail(request):
    form = EmailForm()

    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data['fullname']
            company = form.cleaned_data['company']
            designation = form.cleaned_data['designation']
            from_email = 'python4dia@gmail.com'
            recepient_email = form.cleaned_data['email']
            email_subject = form.cleaned_data['subject']
            msg = form.cleaned_data['message']

            # print(recepient_email)

            Context = {
                'userName':userName,
                'company':company,
                'designation':designation,
                'recepient':recepient_email,
                'subject':email_subject,
                'msg':msg,
            }

            try:
                text_content = msg
                html_content = render_to_string('SendEmailApp/email_content/html_content.html', Context)

                # msg = EmailMultiAlternatives(email_subject, text_content, from_email, [recepient_email])  # if it contains only one email, then put '[]' to make it a list.
                msg = EmailMultiAlternatives(email_subject, text_content, from_email, recepient_email)      # if it contains multiple emails, then doesn't need to put '[]', it is already a list.
                # msg = EmailMultiAlternatives(email_subject, text_content, from_email, ['enamulmajid021@gmail.com', 'shift2unleashed2011@gmail.com'])  # WORKED
                msg.attach_alternative(html_content, "text/html")
                # Check file-attachment
                if request.FILES:
                    files = request.FILES.getlist('attachment')
                    for f in files:
                        msg.attach(f.name, f.read(), f.content_type)
                # msg.send()    # sends email slow
                EmailThread(msg).start()    # sends email fast
                messages.info(request, ('Your email has been sent successfully...'))
            except:
                pass
                messages.error(request, ('Your email has not been sent...'))


    context = {
        'title':'Email Form',
        'form':form,
    }
    return render(request, 'SendEmailApp/SendEmail.html', context)