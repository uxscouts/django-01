from django.urls import path
from . import views

urlpatterns = [
    # The 'name' allows us to reverse the URL in templates
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
]
