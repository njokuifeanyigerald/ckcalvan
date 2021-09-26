from django.shortcuts import render

def home(request):
    context = {

    }
    return render(request, 'alvan/home.html', context)