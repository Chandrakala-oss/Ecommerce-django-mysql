from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import Wishlist,Product
@login_required(login_url="loginpage")
def index(request):
    wishlist =  Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist }
    return render(request,'app/wishlist.html',context)

def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                      return JsonResponse({'status':" product already in wishlist"})  
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id)  
                    return JsonResponse({'status':"Product added to wish list "})      


            else:
                return JsonResponse({'status':"no such product found"})    
        else:
            return JsonResponse({'status':"Login To Continue "})
    return redirect ('/')


def deletewishlistitem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                wishlistitem = Wishlist.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':" product removed from wishlist "})  
            else:
              
                return JsonResponse({'status':"Product not found from wishlist "})  
        else:
            return JsonResponse({'status':"Login To Continue from wishlist "})


    return redirect('/')    