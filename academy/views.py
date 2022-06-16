from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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


# @login_required
# def base(request):
#     return render(request, 'base.html')