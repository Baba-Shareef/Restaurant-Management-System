from django.db import models

# Create your models here.
class Tiffen(models.Model):
    Item = models.CharField(max_length=20)
    Price = models.IntegerField()
class Veglunch(models.Model):
    Item = models.CharField(max_length=20)
    Price = models.IntegerField()
class Vegdinner(models.Model):
    Item = models.CharField(max_length=20)
    Price = models.IntegerField()
class Nonlunch(models.Model):
    Item = models.CharField(max_length=20)
    Price = models.IntegerField()
class Nondinner(models.Model):
    Item = models.CharField(max_length=20)
    Price = models.IntegerField()
class Ctiffen(models.Model):
    Item = models.CharField(max_length=20)
    Price = models.IntegerField()
class Cveglunch(models.Model):
    Item = models.CharField(max_length=20)
    Price = models.IntegerField()
class Cvegdinner(models.Model):
    Item = models.CharField(max_length=20)
    Price = models.IntegerField()
class Cnonlunch(models.Model):
    Item = models.CharField(max_length=20)
    Price = models.IntegerField()
class Cnondinner(models.Model):
    Item = models.CharField(max_length=20)
    Price = models.IntegerField()