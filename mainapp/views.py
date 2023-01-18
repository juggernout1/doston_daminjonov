from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def portfolio_view(request):
    # CONTACT FORM
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message,
        }
        message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Email:\n\t\t{}\n
        Subject:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['subject'])
        send_mail('You got a mail!', message, '', ['doston_daminjonov@mail.ru']) # TODO: enter your email address
        
    return render(request, 'mainapp/index.html', {})
