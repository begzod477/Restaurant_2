from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Chefs, Category, Food, Booking, Testimonial 
from . import models

class Home(View):
    def get(self, request):
        foods = Food.objects.all() 
        return render(request, 'index.html', {'foods': foods})

class About(View):
    def get(self, request):
        return render(request, 'about.html')

class ChefList(View):
    def get(self, request):
        chefs = Chefs.objects.all()  
        return render(request, 'chef_list.html', {'chefs': chefs})

class CategoryList(View):
    def get(self, request):
        categories = Category.objects.all()  
        return render(request, 'category_list.html', {'categories': categories})

class FoodList(View):
    def get(self, request):
        foods = Food.objects.all()  
        return render(request, 'food_list.html', {'foods': foods})

class ChefDetail(View):
    def get(self, request, slug):
        chef = Chefs.objects.get(slug=slug)
        return render(request, 'chef_detail.html', {'chef': chef})

class FoodDetail(View):
    def get(self, request, slug):
        food = Food.objects.get(slug=slug) 
        return render(request, 'food_detail.html', {'food': food})

class Menu(View):
    def get(self, request):
        categories = Category.objects.all()  
        foods = Food.objects.all()  
        return render(request, 'menu.html', {'categories': categories, 'foods': foods})

class TeamView(ListView):
    model = Chefs
    template_name = 'team.html'  
    context_object_name = 'chefs'


class Team(View):
    def get(self, request):
       
        team = Chefs.objects.all()  
        return render(request, 'team.html', {'team': team})

class TestimonialView(View):  
    def get(self, request):
        testimonials = Testimonial.objects.all()  
        return render(request, 'testimonial.html', {'testimonials': testimonials})
class BookingView(View):
    def get(self, request):
        bookings = Booking.objects.all()  
        return render(request, 'booking.html', {'bookings': bookings})

class MenuView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = Category.objects.prefetch_related('foods').all()
        return queryset