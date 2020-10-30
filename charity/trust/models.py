from django.db import models

# Create your models here.

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    occupation = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.BigIntegerField()
    reason = models.CharField(max_length=1000)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=1000)

class Donation(models.Model):
        fname = models.CharField(max_length=100)
        lname = models.CharField(max_length=100)
        email = models.EmailField()
        gender = models.CharField(max_length=100)
        contact = models.BigIntegerField()
        occupation = models.CharField(max_length=100)
        city = models.CharField(max_length=100)
        zipcode = models.BigIntegerField()
        donation_type = models.CharField(max_length=100)
