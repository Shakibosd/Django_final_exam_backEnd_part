from django.db import models
from django.contrib.auth.models import User

#post model
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='admins/images/')
    category = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title

#custome user
class CustomUser(User):
    is_disabled = models.BooleanField(default=False)