from django.shortcuts import render
from django.http import HttpResponse

# A simple view returning text
def home(request):
    return HttpResponse("Hello, this is the home page!")

# A view rendering a template (best practice)
def about_page(request):
    return render(request, 'about.html')
