from django.http import HttpResponseRedirect
from django.shortcuts import render


# from Face.FaceIdentification.classify_webcam import runalgo


def login(request):
    return render(request, 'login.html', {})


def verify(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == "admin@gmail.com" and password == "admin":
        return HttpResponseRedirect('home')
    else:
        return render(request, 'redirect.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Invalid Password or usrername",
                       "path": ""})


def home(request):
    return render(request, 'home.html', {})


def detect_criminal(request):
    # rid = runalgo()
    data = {}
    user1 = {
        "Name": "Yash Hassanandani",
        "Age": "25",
        "Gender": "Male",
        "Number": "9819244040",
        "Crime": "Chain snatching"
    }
    user2 = {
        "Name": "Neha Phulwani",
        "Age": "20",
        "Gender": "Female",
        "Number": "8169344463",
        "Crime": "House theft"
    }
    rid = 1
    if rid == 1:
        data = user1
    if rid == 2:
        data = user2
    print(data)
    return render(request, 'test.html', data)


def test(request):
    return render(request, 'test.html', {})
