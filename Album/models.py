from django.db import models
from musician.models import musician
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
# Create your models here.
class Album(models.Model):
    Album_Name=models.CharField(max_length=50)
    musician_model= models.ForeignKey(musician, on_delete=models.CASCADE, default=None)
    Album_release_date=models.DateField()
    Rating = models.IntegerField()
    tmp = [MaxValueValidator(5),MinValueValidator(0)]

    def __str__(self):
        return self.Album_Name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username