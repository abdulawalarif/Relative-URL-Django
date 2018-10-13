from django.shortcuts import render
app_name = 'relative_url_app'
def index(request):
    return render(request, 'relative_url_app/index.html')

def second(request):
    return render(request, 'relative_url_app/second.html')

def third(request):
    return render(request, 'relative_url_app/third.html')
def base(request):
    return render(request, 'relative_url_app/base.html')
