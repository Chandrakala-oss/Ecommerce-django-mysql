from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from django.contrib import messages
from django.http import HttpResponse
from .models import Product

def test_view(request):
    print("not working ")
    return HttpResponse("It works!")

def index(reqquest):
    return HttpResponse("welcomt o my tention world ")

def hello(request):
    return render(request,"app/index.html ")
    
def hello1(request):
    return render(request,"app/products/home.html ")

def collections(request):
    category =  Category.objects.filter(status=0)
    context = {'category':category}
    
    return render(request,"app/collections.html",context)

def collectionsview(request,slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products = Product.objects.filter(category__slug=slug)
        category= Category.objects.filter(slug=slug).first()
        context={'products':products,'category':category,}
        return render(request,'app/products/index.html',context)
    else:
        messages.warning(request,"no such category found")
        return redirect("collections")

def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(slug=cate_slug,status=0)):
         if(Product.objects.filter(slug=prod_slug,status=0)):
            products =Product.objects.filter(slug=prod_slug,status=0).first()
            context ={'products':products}

         else:
             messages.error(request,"no such product  found") 
             return redirect("collections")  

    else:
        messages.error(request,"no category found") 
        return redirect("collections")  

    return render(request,"app/products/view.html",context)    


def cart_view(request):
    cart_items = request.session.get('cart', {})  # Assuming you're using session to store cart items
    products = Product.objects.filter(id__in=cart_items.keys())
    
    # Create a list of products with their quantities
    cart_details = []
    for Product in products:
        quantity = cart_items[str(product.id)] 
        total_price = product.selling_price * quantity # Convert ID to string for session access
        cart_details.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.selling_price * quantity
        })

    total_amount = sum(item['total_price'] for item in cart_details)

    context = {
        'cart_items': cart_details,
        'total_amount': total_amount,
    }
    return render(request, "app/auth/display.html", context)

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('cart_view') 

def cart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render(request,"app/cart.html",context)   


def proced(request):
    return render(request,"app/auth/cart.html") 

def first(request):
     
    if request.user.is_authenticated:
        messages.warning(request,"you are already login")
        return redirect('/')
    else:
        if request.method== 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request,username=name,password=passwd)

            if user is not None:
               login(request,user)
               messages.success(request,"Logged Successfully")
               return redirect("/")
            else:
               messages.error(request,"Invalid Username or Psswors")
               return redirect("/")
        return render(request,"app/auth/login.html") 