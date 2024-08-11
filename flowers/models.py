from django.db import models
from django.contrib.auth.models import User


class Flower(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='flowers/images/')
    category = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    flower = models.ForeignKey(Flower, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.body[:20]}'