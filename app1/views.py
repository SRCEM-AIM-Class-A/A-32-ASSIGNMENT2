from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')  # Using global template

def about(request):
    return render(request, 'about.html')  # Using global template

