from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/login/')
def lobby(request):
    return render (request, 'base/lobby.html')
