from django.shortcuts import render

def lobby(request):
    return render (request, 'base/lobby.html')
