from django.contrib import admin
from testapp.models import Products
from testapp.models import Order
from testapp.models import checkout
from testapp.models import Order12
from testapp.models import Order123
from testapp.models import feedback
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

class Orderadmin1(admin.ModelAdmin):
    list_dispaly=['firstname','lastname','address','city','payment_method','payment_data','fufulfilled','items']

admin.site.register(Order12,Orderadmin1)

class Orderadmin11(admin.ModelAdmin):
    list_dispaly=['items']
admin.site.register(Order123,Orderadmin11)

class feedbackadmin11(admin.ModelAdmin):
    list_dispaly=['fname','lname','meddage']
admin.site.register(feedback,feedbackadmin11)
