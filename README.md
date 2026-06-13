# django-01

1. Create a virtual environment to isolate dependencies:

python3 -m venv venv
source venv/bin/activate

2. Install Django

pip install django

// verify successful installation

django-admin --version

3. Start Django project
// create project files
// dot at the end is super important and says make here

django-admin startproject myproject .

// run migrations set up database

python

manage.py

 migrate

 error!!!

The error you were getting happened because Django wasn't installed. The correct way to run Django management commands is: ( See, the comands are on the same line)

python manage.py migrate        # Apply migrations
python manage.py makemigrations # Create new migrations
python manage.py runserver  

// set permission on manage.py go to the root with manage.py

chmod +x manage.py

Then use run

 ./manage.py migrate

 3. Start the server

 python manage.py runserver


 // create URL paths links

 create views.py inside project folder

 (views.py) //// [page content]

 from django.shortcuts import render
from django.http import HttpResponse

# A simple view returning text
def home(request):
    return HttpResponse("Hello, this is the home page!")

# A view rendering a template (best practice)
def about_page(request):
    return render(request, 'about.html')


    ////////////////////////////



    2. Connect the View to a URL (urls.py)

     (urls.py) //// [page content]

     from django.urls import path
from . import views

urlpatterns = [
    # The 'name' allows us to reverse the URL in templates
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
]


/////////////////////////////////

// file: myapp/templates/home.html

html<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome Home</h1>
    <!-- Link to the 'about' path defined in urls.py -->
    <a href="{% url 'about' %}">Go to About Page</a>
</body>
</html>