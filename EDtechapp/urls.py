from django.contrib import admin
from django.urls import path
from EDtechapp import views


urlpatterns = [
    path('', views.index, name='Home'),
    path("About Us", views.About, name='About Us'),
    path("Courses", views.Courses, name='Courses'),
    path("Contact", views.Contact, name='Contact Us'),
    path("Login", views.Login, name='Login'),

]
