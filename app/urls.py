
from django.urls import path 

from .import views

from django.urls import path
from .views import test_view
from app.Controller import authview,cart,wishlist,checkout
urlpatterns = [
    path('test/', test_view, name='test'),
    path('index',views.index),
    path('',views.hello,name="home"),
    path('hello1',views.hello1,name="hello1"),
    path('collections',views.collections,name='collections'),
    path('collections/<slug:slug>',views.collectionsview,name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name="productview"),
    path('register/',authview.register,name="register"),
    path('login/',authview.loginpage,name="loginpage"),
    path('logout/',authview.logoutpage,name="logout"),
    path('add-to-cart',cart.addtocart,name="addtocart"),
    path('cart',cart.viewcart, name='cart'),
    path('update-cart',cart.updatecart,name='updatecart'),
    path('delete-cart-item',cart.deletecartitem,name='deletecartitem'),
    path('wishlist',wishlist.index,name='wishlist'),
    path('add-to-wishlist',wishlist.addtowishlist,name="addtowishlist"),
    path('delete-wishlist-item',wishlist.deletewishlistitem,name="deletewishlistitem"),
    path('checkout',checkout.index,name='checkout'),
    path('place-order',checkout.placeorder,name='placeorder'),
    path('proceed-to-pay',checkout.razorpaycheck,name='razorpaycheck'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('proced',views.proced,name='proced'),
    path("first/",views.first,name="first")
    

]

