from django.contrib import admin
from testapp.models import Products
from testapp.models import Order
from testapp.models import checkout
# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display=['name','price','description','imglink']

admin.site.register(Products,ProductsAdmin)


class Orderadmin(admin.ModelAdmin):
    list_dispaly=['name','product_name','quantity','contact_no','address']

admin.site.register(Order,Orderadmin)

class checkoutadmin(admin.ModelAdmin):
    list_display=['ordered_item','address','contact_no']

admin.site.register(checkout,checkoutadmin)
