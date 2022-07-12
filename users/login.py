from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def UserLoginForm(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('base')
        else:
            messages.info(request, 'Daxil etdiyiniz istifadçi adı/şifrəsi yalnışdır və ya hesab təsdiqlənməmişdir. Hesabın təsdiqlənməsi üçün e-poçt adresinizə göndərilən linkə keçin.')
            return redirect('login')

    else:
        return render(request, 'users/login.html', {'title': 'Blockchain Academy'})