from django.shortcuts import render

# Create your views here.


def home(request):
    length = list(range(6, 25))
    return render(request, 'home.html', {'lst': length})


def password(request):
    return render(request, 'password.html')

