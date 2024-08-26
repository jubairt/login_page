from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.cache import never_cache
from .forms import LoginForm


@never_cache
def tohome(request):
        if not request.user.is_authenticated:
            return redirect('logIn')
        if request.user:
            return render(request,'home.html')
        else:
            return redirect('logIn')
        


@never_cache
def logIn(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def tologout(request):
    logout(request)
    return redirect('logIn')

def practice(request):
    data={
        'name':'jubair'

    }
    return render(request,'pract.html',data)


# Create your views here.
