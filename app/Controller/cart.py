from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
from app.models import Product,Cart

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                prod_id = request.POST.get('product_id')
                prod_qty = request.POST.get('product_qty')

                if prod_id is None or prod_qty is None:
                    return JsonResponse({'status': "Product ID and quantity are required"})

                prod_id = int(prod_id)
                prod_qty = int(prod_qty)

                product_check = Product.objects.get(id=prod_id)

                if product_check:
                    if Cart.objects.filter(user=request.user.id, product_id=prod_id).exists():
                        return JsonResponse({'status': "Product already in cart"})
                    else:
                        if product_check.quantity >= prod_qty:
                            Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                            return JsonResponse({'status': "Product added successfully"})
                        else:
                            return JsonResponse({'status': f"Only {product_check.quantity} quantity available"})
                else:
                    return JsonResponse({'status': "No such product found"})
            except Product.DoesNotExist:
                return JsonResponse({'status': "No such product found"})
            except ValueError:
                return JsonResponse({'status': "Invalid product ID or quantity"})
            except Exception as e:
                return JsonResponse({'status': f"An error occurred: {str(e)}"})
        else:
            return JsonResponse({'status': "Login to continue"})

    return JsonResponse({'status': "Invalid request method"})

@login_required(login_url='loginpage')
def viewcart(request):
    cart  = Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render(request,"app/auth/cart.html",context)
def updatecart(request):
    if request.method == 'POST':
        prod_id = request.POST.get('product_id')
        product_qty = request.POST.get('product_qty')

        if prod_id is None or product_qty is None:
            return JsonResponse({'status': "Product ID or Quantity is missing"}, status=400)

        try:
            prod_id = int(prod_id)
            product_qty = int(product_qty)

            if Cart.objects.filter(user=request.user, product_id=prod_id).exists():
                cart = Cart.objects.get(product_id=prod_id, user=request.user)
                cart.product_qty = product_qty  # Update quantity
                cart.save()
                return JsonResponse({'status': "Updated successfully"})
            else:
                return JsonResponse({'status': "Product not found"}, status=404)
        except ValueError:
            return JsonResponse({'status': "Invalid input"}, status=400)

    return JsonResponse({'status': "Invalid request"}, status=400)

def deletecartitem(request):
    if request.method =='POST' :
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            cartitem =Cart.objects.get(product_id=prod_id,user=request.user)
            cartitem.delete()
        return JsonResponse({'status':"Deleted Successfully"})  
    return redirect('/')      


