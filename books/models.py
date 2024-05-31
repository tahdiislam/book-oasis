from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    image = models.ImageField(upload_to='books/media/uploads/', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title