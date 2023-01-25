from django.shortcuts import render
from .import models
from testapp.models import Products
from testapp.models import checkout
from testapp import forms
from django.shortcuts import redirect
# Create your views here.
def cartItems(cart):
    items = []
    for item in cart:
        items.append(Products.objects.get(id=int(item)))
    return items




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

    form=forms.CheckForm
    if request.method=='POST':
        form=forms.CheckForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/thanks/')
    ctx={'cart':cart, 'cart size':len(cart),'store_item':store_item,'cart_items':cartItems(cart),'form':form}



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


    return render(request,'html/bv.html',{'form':form})
def thanks(request):
    return render(request,'html/thanks.html')
