from django.db import models


# sqlmigrate main_app 0001_initial
class Shoe(models.Model):
    brand = models.CharField(max_length=25)
    size = models.PositiveIntegerField()


# makemigrations main_app --name migrate_unique_brands --empty
class UniqueBrands(models.Model):
    brand_name = models.CharField(max_length=25)
