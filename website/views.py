from django.shortcuts import render

def home(request):
    # Fetch latest news, tutorials, strategies
    context = {
        'home': 'home',
    }
    return render(request, 'index.html', context)

def about(request):
    # Fetch latest news, tutorials, strategies
    context = {
        'about': 'about',
    }
    return render(request, 'about.html', context)

def contact(request):
    # Fetch latest news, tutorials, strategies
    context = {
        'contact': 'contact',
    }
    return render(request, 'contact.html', context)

def portfolio(request):
    # Fetch latest news, tutorials, strategies
    context = {
        'portfolio': 'portfolio',
    }
    return render(request, 'portfolio.html', context)