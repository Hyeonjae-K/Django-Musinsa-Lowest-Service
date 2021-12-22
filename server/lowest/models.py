from django.db import models


class Brands(models.Model):
    ko_name = models.CharField(max_length=64)
    en_name = models.CharField(max_length=64)
    url = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    created_date = models.DateTimeField()


class History(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    price = models.IntegerField()
    created_date = models.DateTimeField()


class Products(models.Model):
    name = models.CharField(max_length=128)
    brand = models.ForeignKey('Brands', on_delete=models.SET_NULL, null=True)
    current = models.ForeignKey(
        'History', on_delete=models.SET_NULL, null=True, related_name='current')
    lowest = models.ForeignKey(
        'History', on_delete=models.SET_NULL, null=True, related_name='lowest')
    highest = models.ForeignKey(
        'History', on_delete=models.SET_NULL, null=True, related_name='highest')
    url = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    created_date = models.DateTimeField()
