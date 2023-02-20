from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")



def products(request):
    products=[
        {'name':'bread','price':1,'quantity':20},
        {'name':'milk','price':1.6,'quantity':30},
        {'name':'wine','price':6,'quantity':10}
    ]

    context={
        'products':products
    }
    return render(request,"products.html",context)
def justproduct(request):
    products=[
        {'name':'bread','price':1,'quantity':20},
        {'name':'milk','price':1.6,'quantity':30},
        {'name':'wine','price':6,'quantity':10}
    ]

    context={
        'products':products
    }
    return render(request,"JustProduct.html",context)



def customers(request):
    Person={
        'firstName':'Tornike',
        'lastName':'Chilashvili'

    }
    return render(request,"customers.html",{'person':Person})