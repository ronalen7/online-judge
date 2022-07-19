from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def Login(request):
    if request.method == 'POST':
        # form = AuthenticationForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # if form.is_valid():
        if user is not None:
            # log in user
            # user = form.get_user()
            login(request, user)
            return redirect('onlineJudge:index')

        else:
            return HttpResponse("Invalid User!")

    else:
        form = AuthenticationForm()

    return render(request, 'authentication/login.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('authentication:login')


def Home(request):
    return render(request, 'authentication/home.html')
