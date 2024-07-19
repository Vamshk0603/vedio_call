from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as django_logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                auth_login(request, user)
                return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')   # Redirect to home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html',{'name':request.user.username})

def meeting(request):
    return render(request, 'vediocall.html',{'username':request.user.username})

def logout(request):
    django_logout(request)
    return redirect('login')

def joinmeeting(request):
    if request.method=='POST':
        roomID=request.POST['roomID']
        return redirect('meeting') 
    return render(request, 'joinmeeting.html')

    