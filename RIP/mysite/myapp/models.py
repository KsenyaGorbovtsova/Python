from django.db import models

# Create your models here.

class Band(models.Model):
    name=models.CharField(max_lenght=20)
    origin=models.CharField(max_lenght=50)
    genre=models.CharField(max_lenght=50)
    founding_date=models.DateField()
    description=models.TextField()
    image=models.ImageField(upload_to='')

class Artist(models.Model):
    band=models.ForeignKey(Band)
    GENDER_CHOICES=(
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    first_name=models.CharField(max_lenght=20)
    last_name=models.CharField(max_lenght=20)
    gender=models.CharField(max_lenght=2, choices=GENDER_CHOICES)
    instrument=models.CharField(max_lenght=20)
    photo=models.ImageFiled(upload_to='')



