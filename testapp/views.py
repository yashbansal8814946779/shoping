from django.shortcuts import render
from .import models
from testapp.models import Products
from testapp.models import checkout
from testapp.models import Order12
from testapp.models import Order123
from testapp.models import feedback
from testapp import forms
from django.shortcuts import redirect
# Create your views here.
def cartItems(cart):
    items = []
    for item in cart:
        items.append(Products.objects.get(id=int(item)))
    return items

def pricecart(cart):
    cart_item=cartItems(cart)
    price=0
    for item in cart_item:
        price=price+item.price
    return price

def itemlist(cart):
    cart_item=cartItems(cart)
    item_list=""
    for item in cart_item:
        item_list+=","
        item_list+=item.name
    return item_list

def removefromcart(request):
        if request.method == "POST":
            request.session.set_expiry(0)
            obj_to_remove = request.POST['obj_id1']
            obj_indx = request.session['cart'].index(obj_to_remove)
            request.session['cart'].pop(obj_indx)
            return redirect('/hello/cart')


def catalog(request):
    if 'cart' not in request.session:
        cart= []


        request.session['cart']=[]

    cart= request.session['cart']
    request.session.set_expiry(0)
    store_item= Products.objects.all()
    ctx={'store_item': store_item , 'cart_size' :len(cart)}

    if request.method == "POST":
        cart.append(request.POST['obj_id'])


        return redirect('/hello/')


    return render(request,'html/catalog.html',ctx)




def cart(request):
    cart=request.session['cart']

    request.session.set_expiry(0)
    store_item= Products.objects.all()


    ctx={'cart':cart, 'cart size':len(cart),'store_item':store_item,'cart_items':cartItems(cart),'price':pricecart(cart)}



    return render(request,'html/cart.html',ctx)





def contact(request):
    return render(request,'html/contact.html')

def contacts(request):
    return render(request,'html/bv.html')
def ordernow(request):
    form=forms.OrderForm
    if request.method=='POST':
        form=forms.OrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/thanks/')



    return render(request,'html/bv.html',{'form':form})
def thanks(request):
    return render(request,'html/thanks.html')


def completeOrder(request):
    cart = request.session['cart']
    request.session.set_expiry(0)
    ctx = {'cart':cart, 'cart_size':len(cart), 'cart_items':cartItems(cart), 'total_price': pricecart(cart)}
    order = Order12()
    order.items = itemlist(cart)
    order.firstname = request.POST.get('firstname',False)
    order.lastname = request.POST.get('lastname',False)
    order.address = request.POST.get('address',False)
    order.city = request.POST.get('city',False)
    order.payment_data = request.POST.get('payment_data',False)
    order.fulfilled = False
    order.payment_method = request.POST.get('payment',False)
    order.save()
    request.session['cart'] = []
    return render(request, "html/thanks.html", ctx)

def completeOrder11(request):
    cart = request.session['cart']
    request.session.set_expiry(0)
    ctx = {'cart':cart, 'cart_size':len(cart), 'cart_items':cartItems(cart), 'total_price': pricecart(cart)}
    order = Order123()
    order.items = itemlist(cart)
    order.save()
    request.session['cart'] = []
    return render(request, 'html/thanks.html', ctx)


def checkout(request):
    cart = request.session['cart']
    request.session.set_expiry(0)
    ctx = {'cart':cart, 'cart_size':len(cart), 'cart_items':cartItems(cart), 'total_price': pricecart(cart)}
    return render(request, "html/checkout.html", ctx)
