from django.db import models

# Create your models here.


class Chefs(models.Model):
    name = models.CharField(max_length=100, verbose_name='oshpaz ismi', blank=True)
    slug = models.SlugField(max_length=100, verbose_name = 'oshpaz ismi')
    description = models.TextField(blank=True, verbose_name='oshpaz haqida')
    image = models.ImageField(upload_to='chefs/', verbose_name='oshpaz rasmi')
    age = models.IntegerField(default=18, verbose_name='ochpazni yoshi')
    designation = models.CharField(max_length=75, verbose_name='lavozmi', blank=True)

    

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ('Oshpaz')
        verbose_name_plural = 'Oshpazlar'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='ovqat kategoriyasi nomi')
    description = models.TextField(blank=True, verbose_name='ovqat kategoriyasi tavsifi')
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('Ovqat kategiriyasi')
        verbose_name_plural = 'Ovqat kategiriyalari'

class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name='ovqat nomi')
    slug = models.SlugField(max_length=160, unique=True)
    description = models.TextField(verbose_name='ovqat haqida')
    image = models.ImageField(upload_to='food/', verbose_name='ovqat rasmi')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='ovqat narxi $')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods')  
    discount = models.IntegerField(null=True, blank=True, verbose_name="Chegirma (%)")
    chef = models.ForeignKey(Chefs, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Ovqat')
        verbose_name_plural = 'Ovqatlar'


class Booking(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name='Mijoz ismi')
    booking_date = models.DateTimeField(verbose_name='Buyurtma sanasi')
    people_count = models.IntegerField(default=1, verbose_name='Insonlar soni')
    special_requests = models.TextField(blank=True, verbose_name='Maxsus talablar')

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'
class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ismi')
    message = models.TextField(verbose_name='Xabar')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

