from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages

import environ
env = environ.Env()
environ.Env.read_env()

def academy(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        data = {
            'email' : email,
            'message' : 'We have a new subscribed user!'
        }

        message = '''

        New message: {}

        E-mail: {}
        
        '''.format(data['message'], data['email'])
        
        messages.success(request, f'{email} uğurla abunə oldu!') 
        send_mail("New subscription", message, '', [env('EMAIL_HOST_USER')])
        return redirect('academy')

    return render(request, 'index.html', {'title': 'Blockchain Academy'})

def technical(request):
    return render(request, 'technical.html', {'title': 'Blockchain Academy'})

def fundamental(request):
    return render(request, 'fundamental.html', {'title': 'Blockchain Academy'})

def priceaction(request):
    return render(request, 'priceaction.html', {'title': 'Blockchain Academy'})

def entrytocrypto(request):
    return render(request, 'entrytocrypto.html', {'title': 'Blockchain Academy'})

def riskmanagement(request):
    return render(request, 'riskmanagement.html', {'title': 'Blockchain Academy'})

def ticaretstrategy(request):
    return render(request, 'ticaretstrategy.html', {'title': 'Blockchain Academy'})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        if name:
            email = request.POST.get('email')
            number = request.POST.get('number')
            message = request.POST.get('message')

            data = {
                'name' : name,
                'email' : email,
                'number' : number,
                'message' : message
            }

            message = '''   
            
            New message: {}

            E-mail: {}

            Number: {}
            '''.format(data['message'], data['email'], data['number'])

            messages.success(request, f'İsmarıcınız uğura göndərildi') 
            con = 1
            send_mail(data['name'], message, '', [env('EMAIL_HOST_USER')], con)
            return redirect('contact')

        else:
            email = request.POST.get('email')

            data = {
                'email' : email,
                'message' : 'We have a new subscribed user!'
            }

            message = '''
            
            New message: {}

            E-mail: {}
            
            '''.format(data['message'], data['email'])
            
            messages.success(request, f'{email} uğurla abunə oldu!') 
            send_mail("New subscription", message, '', [env('EMAIL_HOST_USER')])
            return redirect('contact')

    return render(request, 'contact.html', {'title': 'Blockchain Academy'})

def faq(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        data = {
            'email' : email,
            'message' : 'We have a new subscribed user!'
        }

        message = '''
        
        New message: {}

        E-mail: {}
        
        '''.format(data['message'], data['email'])
        
        messages.success(request, f'{email} uğurla abunə oldu!') 
        send_mail("New subscription", message, '', [env('EMAIL_HOST_USER')])
        return redirect('faq')
        
    return render(request, 'faq.html', {'title': 'Blockchain Academy'})


