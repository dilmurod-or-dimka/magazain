from django.shortcuts import render

# Create your views here.


def login_view(request):
    return render(request, "pages/login.html")


def registration_view(request):
    return render(request, "pages/registration.html")
