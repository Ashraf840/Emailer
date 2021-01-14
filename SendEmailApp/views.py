from django.shortcuts import render
from .forms import EmailForm
from django.contrib import messages


# Account Activation HTML Templated Email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template import Context



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
            from_email = 'python4dia@gmail.com'
            recepient_email = form.cleaned_data['email']
            email_subject = form.cleaned_data['subject']
            msg = form.cleaned_data['message']

            Context = {
                'recepient':recepient_email,
                'subject':email_subject,
                'msg':msg,
            }

            try:
                text_content = msg
                html_content = render_to_string('SendEmailApp/email_content/html_content.html', Context)

                msg = EmailMultiAlternatives(email_subject, text_content, from_email, [recepient_email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                messages.info(request, ('Your email has been sent successfully...'))
            except:
                pass
                messages.error(request, ('Your email has not been sent...'))


    context = {
        'title':'Email Form',
        'form':form,
    }
    return render(request, 'SendEmailApp/SendEmail.html', context)