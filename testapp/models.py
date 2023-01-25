from django.db import models

# Create your models here.
class Products(models.Model):
    name= models.CharField(max_length=850)
    price = models.FloatField()
    description=models.TextField()
    imglink=models.CharField(max_length=850)


class Order(models.Model):
    name=models.CharField(max_length=30)
    product_name = models.CharField(max_length=200)
    quantity= models.IntegerField()
    contact_no = models.CharField(max_length=250)
    address=models.CharField(max_length=200)

class checkout(models.Model):
    ordered_item=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    contact_no=models.CharField(max_length=200)
