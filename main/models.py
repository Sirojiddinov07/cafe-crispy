from django.db import models
from django.contrib.auth.models import User





class Foods(models.Model):
    status =(
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
    )
    status2 = (
        ('foods', 'foods'),
        ('drink', 'drink'),
        ('salad', 'salad'),
        ('desert', 'desert'),
    )
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/')
    special = models.CharField(max_length=100, choices=status)
    rating = models.PositiveIntegerField()
    price = models.FloatField()
    discount_price = models.FloatField( null=True, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=status2, default='foods')

    def __str__(self):
        return self.name



class News(models.Model):
    status = (
        ('t', 'featured'),
        ('promotion', 'promotion'),
        ('news', 'news'),
        ('meeting', 'meeting'),
    )
    name =models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100, choices=status)

    def __str__(self):
        return self.name

class About(models.Model):
    header = models.CharField(max_length=300)
    text = models.TextField()

    def __str__(self):
        return self.header


class Team(models.Model):
    name = models.CharField(max_length=100)
    type_of_job = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/')
    description = models.TextField()
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField()
    message = models.TextField()

class Reserve(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    num_person = models.IntegerField()
    date = models.DateTimeField()
    time = models.CharField(max_length=100)
    request = models.TextField()



