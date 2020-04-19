from django.http import HttpResponseRedirect
from django.shortcuts import render


def login(request):
    return render(request, 'login.html', {})

def verify(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == "admin@gmail.com" and password == "admin":
        return HttpResponseRedirect('/home')
    else:
        return render(request, 'redirect.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Invalid Password or usrername",
                       "path": ""})


def home(request):
    return render(request, 'home.html', {})

def detect_criminal(request):

    return render(request, 'home.html', {})
def test(request):

    return render(request, 'test.html', {})
