from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def typography(request):
    return render(request, 'typography.html')

def contacts(request):
    return render(request, 'contacts.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'This Email already exists on our database')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Your Username is so cool, it already exists. Type in another one')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Hmmm... These passwords don\'t look the same')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Whoops. Seems you might\'ve typed in something different')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def account(request, uname): 
    return render (request, 'account.html', {'uname': uname})

def cart(request):
    return render(request, 'cart.html')