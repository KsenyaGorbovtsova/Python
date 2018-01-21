import pymysql
from django.db import models


class Band(models.Model):
    name = models.CharField()
    origin = models.CharField()
    genre = models.CharField()
    founding_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='')


class Artist(models.Model):
    band = models.ForeignKey(Band)
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    first_name = models.CharField()
    last_name = models.CharField()
    gender = models.CharField(choices=GENDER_CHOICES)
    instrument = models.CharField()
    photo = models.ImageFiled(upload_to='')
