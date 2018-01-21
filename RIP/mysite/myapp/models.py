from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=20)
    origin = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    founding_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='media')


class Artist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    band = models.ForeignKey(Band, null=True)

    def save(self, *args, **kwargs):
        if self.band is None:
            self.band = Band.objects.get(id=14)
        super(Artist, self).save(*args, **kwargs)

    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    first_name = models.TextField(max_length=20, default='')
    last_name = models.TextField(max_length=20, default='')
    gender = models.TextField(max_length=20, choices=GENDER_CHOICES, default='')
    instrument = models.TextField(max_length=20, default='')

    @receiver(post_save, sender=User)
    def create_user_artist(sender, instance, created, **kwargs):
        if created:
            Artist.objects.create(user=instance)
