from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    dob = models.DateTimeField()
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)
    coach = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    image = models.ImageField(upload_to='registration_images')

    def __str__(self):
        return self.name


# Create your models here.
