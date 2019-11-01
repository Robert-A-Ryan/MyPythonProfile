from django.shortcuts import render, render_to_response

def index(request):
    return render_to_response('index.html',{'title': 'Home'})

def about(request):
    return render_to_response('about.html',{'title': 'About'})

def portfolio(request):
    return render_to_response('portfolio.html',{'title': 'Portfolio'})

def socials(request):
    return render_to_response('socials.html',{'title': 'Socials'})

def contact(request):
    return render_to_response('contact.html',{'title': 'Contact'})
