from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Photo(models.Model):
    sno=models.AutoField(primary_key=True)
    img_file=models.ImageField(upload_to="profilepictures")

    def __str__(self):
        return str(self.img_file)
    
class Post(models.Model):
    title=models.CharField(max_length=122)
    content=models.CharField(max_length=122)
    name=models.CharField(max_length=122)
    date=models.DateField()

    def __str__(self):
        return self.title
    