from django.db import models


# Create your models here.

class Profile(models.Model):
    RELIGION = (
        ('Muslim', 'Muslim'),
        ('Hindu', 'Hindu'),
        ('Christian', 'Christian'),
        ('Bouddho', 'Bouddho'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'others'),
    )

    name = models.CharField(max_length=25, null=True, blank=True)
    image = models.ImageField(upload_to='Profile_pic/', default='default/def.jpg', blank=True, null=True)
    Email = models.EmailField(max_length=50, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True)
    phone_no = models.TextField(max_length=20, blank=True, null=True)
    date_of_birth = models.TextField(max_length=12, blank=True, null=True)
    religion = models.CharField(max_length=9, choices=RELIGION)
    gender = models.CharField(max_length=6, choices=GENDER)

    def __str__(self):
        return str(self.name)
