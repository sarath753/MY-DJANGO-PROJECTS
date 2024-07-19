from django.urls import path
from . import views

urlpatterns = [
    path('productshome/',views.products_view,name="simpleproductdisplay"),
    path('productentry/',views.add_product,name="productentry"),
    path('addtocartsingle/<int:id>',views.add_tocart,name="addtocart"),
    path('cartdelete/<int:id>',views.cartdelete,name="cartdelete"),
    path('cartdisplay/',views.cartdisplay,name="cartdisplay"),
]