from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def resources(request):
    return render(request, 'resources.html')

def about(request):
    return render(request, 'about.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms(request):
    return render(request, 'terms.html')

def refund_policy(request):
    return render(request, 'refund_policy.html')