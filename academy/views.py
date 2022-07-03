from django.shortcuts import render
from django.core.mail import send_mail

def academy(request):
    return render(request, 'index.html', {'title': 'Blockchain Academy'})

# What do we teach?

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

        send_mail(data['name'], message, '', ['aykhan.mv@gmail.com'])

    return render(request, 'contact.html', {'title': 'Blockchain Academy'})

def faq(request):
    return render(request, 'faq.html', {'title': 'Blockchain Academy'})


