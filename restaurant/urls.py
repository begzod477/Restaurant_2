from django.urls import path
from .views import (Home, About, ChefList, CategoryList, FoodList, ChefDetail, FoodDetail, Menu, TeamView, Booking, Team, TestimonialView, BookingView, MenuView, TeamView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('chefs/', ChefList.as_view(), name='chef_list'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('foods/', FoodList.as_view(), name='food_list'),
    path('chef/<slug:slug>/', ChefDetail.as_view(), name='chef_detail'),
    path('food/<slug:slug>/', FoodDetail.as_view(), name='food_detail'),
    path('menu/', Menu.as_view(), name='menu'),  
    path('team/', TeamView.as_view(), name='team'),
    path('booking/', BookingView.as_view(), name='booking'),  
    path('team/', Team.as_view(), name='team_detail'),
    path('testimonials/', TestimonialView.as_view(), name='testimonials'),
    path('index/', MenuView.as_view(), name='menu'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
