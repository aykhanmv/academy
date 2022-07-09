class loginform(View):

    template_name='essay/Login.html'
    form_class=UserForm

    def get(self,request):     # if the request is get then only view the function
        form=self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            #user = form.save(commit=False)  # it doesnot save in database, it is used to et clean the values
            # clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # authenticate user:
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                if(request.user.is_prof==True):
                    return redirect('essay:file', )
                else:
                    return redirect('essay:stdprofile')
            else:
                return render(request,self.template_name, {
                    'error_message': ' Login Failed! Enter the username and password correctly', })
        else:
            msg = 'Errors: %s' % form.errors.as_text()
            return HttpResponse(msg, status=400)

        return render(request, self.template_name, {'form': form})