from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Sum
from .models import Products,cartitems

def products_view(request):
    category = request.GET.get('category', '')
    if category:
        products = Products.objects.filter(category__icontains=category)
    else:
        products = Products.objects.all()
    return render(request, 'products/products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        product = Products(
                name=name,
                category=category,
                price=float(price),
                description=description,
                image=image
        )
        product.save()
        return redirect('simpleproductdisplay')  # Redirect to a product list view or another view of your choice

    return render(request, 'products/productentry.html')


def add_tocart(request,id):
    item = get_object_or_404(Products,id=id)
    cartitem = cartitems(name= item.name,
                category= item.category,
                price=float(item.price),
                description= item.description,
                image= item.image)
    cartitem.save()
    return redirect('simpleproductdisplay')

def cartdisplay(request):
    cartentry = cartitems.objects.all()
    total_cost = cartitems.objects.aggregate(total_price=Sum('price'))['total_price'] or 0
    return render(request,'products/cart.html',{
        'cartentry': cartentry,
        'total_cost': total_cost
    })

def cartdelete(request,id):
    item = get_object_or_404(cartitems,id=id)
    item.delete()
    return redirect('cartdisplay')
