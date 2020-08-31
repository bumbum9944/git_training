from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests, 'home.html')


def gibeom(requests):
    return render(requests, 'gibeom.html')