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

class Order12(models.Model):
    firstname = models.CharField(max_length=400)
    lastname = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=400)
    payment_method = models.CharField(max_length=400)
    payment_data = models.CharField(max_length=400)
    fulfilled = models.BooleanField()
    items = models.TextField()
class Order123(models.Model):
    items = models.TextField()
class feedback(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    message=models.TextField()
