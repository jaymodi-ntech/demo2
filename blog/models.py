from django.db import models

# Create your models here.

class blog_user(models.Model):
    gender_choice=(
        ('m', 'Male'),
        ('f', 'Female'),
    )
    name = models.CharField( max_length=30)
    address = models.TextField(max_length= 70)
    age = models.IntegerField(max_length= 10)
    contact= models.IntegerField(max_length=15)
    city = models.CharField(max_length= 30)
    gender=models.CharField(max_length=1, choices=gender_choice)
    username = models.CharField(max_length= 25)
    password = models.CharField(max_length=15)

    def __unicode__(self):
        return self.username

