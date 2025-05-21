from django.shortcuts import render

from django.http import HttpResponse

def index_view(request):
    return render(request, 'app/index.html')

def about_view(request):
    return render(request, 'app/about.html')

def contact_view(request):
    return render(request, 'app/contact.html')
 
def test_view(request):
    return render(request, 'app/test.html', {'name': 'Arian', 'lastname': 'Amirpour'})