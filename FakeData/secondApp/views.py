from django.shortcuts import render
from .models import Product
import requests

# Create your views here.

def index(request):
    pros = Product.objects.all()
    context = {'products': pros}
    return render(request, 'secondApp/index.html',context)

def product(request, id):
    prod = Product.objects.get(pk=id)
    recently_viewed = None
    if 'recently_viewed' in request.session:
        if id in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(id)
            # note pk is id only, you can do id__in i think
            # retrieves all the products having id's present in request.session['recently_viewed']
        recently_viewed = Product.objects.filter(pk__in=request.session['recently_viewed'])
        # print("ok")
        request.session['recently_viewed'].insert(0,id)
        if len(request.session['recently_viewed']) >5:
            request.session['recently_viewed'].pop()
    else:
        request.session['recently_viewed'] = []
        request.session['recently_viewed'].append(id)

    # Django Don't know sessions in middleware was updated or not
    # so we need to tell django that we are updating the Sessions
    request.session.modified = True
    context = {
        "title": prod.title,
        "price": prod.price,
        "description": prod.description,
        "image": prod.image_url, 
        'recently_viewed': recently_viewed,
    }
    return render(request, 'secondApp/product.html',context)

def load_products(request):
    r = requests.get("https://fakestoreapi.com/products")
    # print(r.json())
    for item in r.json():
        product = Product(
            title=item['title'],
            description=item['description'],
            price=item['price'],
            image_url=item['image']
        )
        product.save()
    # for item in r.json():
    #     Product.objects.create(title1=item['title'],price=item['price'],description=item['description'],image_url=item['image'])
        # i1.save()
    return render(request, 'secondApp/index.html')
    
