from django.db import models

# Create your models here.

class blog_user(models.Model):
    gender_choice=(
        ('m', 'Male'),
        ('f', 'Female'),
    )
    name = models.CharField( max_length=30)
    address = models.TextField(blank=True,null=True)
    age = models.IntegerField()
    contact= models.IntegerField()
    city = models.CharField(max_length= 30)
    gender=models.CharField(max_length=1, choices=gender_choice,blank=True,null=True)
    username = models.CharField(max_length= 25)
    password = models.CharField(max_length=15)

    def __unicode__(self):
        return self.username