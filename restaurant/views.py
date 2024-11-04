from django.shortcuts import render, redirect
from django.views import View
from .models import Chefs, Category, Food,  Review

class Home(View):
    def get(self, request):
        chefs = Chefs.objects.all()
        foods = Food.objects.all()
        categories = Category.objects.all() 
        reviews = Review.objects.all()
        context = {
            'foods': foods,
            'chefs': chefs,
            'categories': categories,
            'reviews': reviews,
        }
        return render(request, 'index.html', )
    
    def post(self, request):
        try:
            full_name = request.GET.get["full_name"]
            profession = request.GET.get["profession"]
            text = request.POST.get["text"]
            rate = request.POST.get["rate"]

            if full_name and profession and text and rate:
                print("test bu ---------------------")
                if request.user.is_authenticated:
                    review = Review.objects.create(
                        text=text,
                        rate=rate,
                        user=request.user,
                        full_name=full_name,
                        profession=profession,
                        rating=int(rate)
                        
                    )
                return redirect('home')
        except :
            pass
        return redirect('home')