from django.shortcuts import render

def app1_home(request):
    return render(request, 'App1/home.html')
