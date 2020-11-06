from django.db import models
import uuid

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

class Regulardonation(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, unique=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    occupation = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.BigIntegerField()
    type = models.CharField(max_length=100)
    amount = models.BigIntegerField(blank=True,null=True)
    checksum_id = models.CharField(max_length=100, default=0)


class Anonymousdonation(models.Model):
    uuid = models.UUIDField(
         default=uuid.uuid4, unique=True)
    zipcode = models.BigIntegerField()
    type = models.CharField(max_length=100)
    amount = models.BigIntegerField(blank=True,null=True)
    checksum_id = models.CharField(max_length=100, default=0)
