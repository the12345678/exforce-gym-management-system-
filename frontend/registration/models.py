
from django.db import models


class GymMember(models.Model):
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    dob = models.DateField() 
    #dob = models.DateTimeField()

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mail = models.EmailField()
    phone_num = models.CharField(max_length=12)
   # COACH_CHOICES = [
    #    ('coach1', 'Mr. Dilshan Samaranayaka'),
    #    ('coach2', 'Mr. Naveen Suranimala'),
    #    ('coach3', 'Mr. Dilruwan Hettiarachchi'),
    #    ('coach4', 'Mr. Chamath Sandaru'),
    #]
   # coach = models.CharField(max_length=10, choices=COACH_CHOICES)
   # PURPOSE_CHOICES = [
     #   ('purpose1', 'Cosmetic user'),
     #   ('purpose2', 'Competitive body builder'),
      #  ('purpose3', 'Recreational body builder'),
     #   ('purpose4', 'Glucose level controller'),
     #   ('purpose5', 'Blood pressure controller'),
     #   ('purpose6', 'Sports user'),
   # ]
    #purpose = models.CharField(max_length=10, choices=PURPOSE_CHOICES)
   # image = models.ImageField(upload_to='images/')

    
    def __str__(self):
        return self.name

# Create your models here.
