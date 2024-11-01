from django.contrib import admin
from .models import Chefs, Food, Category

# Register your models here.

@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


    