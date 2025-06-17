from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# from .models import Products
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Products, Newlist, Featuredproducts, Category, Signup, Cart, Order, Contact


def HomePage(request):
    print(request.session)
    return render(request,'Home.html')


def LoginPage(request):

    return render(request, 'login.html')


def SignupPage(request):
    return render(request, 'signup.html')


def MainPage(request):
    print(request.session)
    data = Products.objects.all()[:8]
    user = Newlist.objects.all()
    items = Featuredproducts.objects.all()
    view = Category.objects.all()

    return render(request, 'main.html', {"data":data, "user":user, "items":items, "view":view })


def ProductPage(request):
    viewId = request.GET.get('id')

    data = get_object_or_404(Products, id=viewId)

    return render(request, 'product.html', {'data': data})

def GendarItem(request):
    # Get the value from query parameter 'forusing'
    forusing = request.GET.get('forusing')

    # If no filter provided, show all products or handle differently
    if not forusing:
        products = Products.objects.all()  # or .filter() with some default condition
        return render(request, 'categories.html', {"items": products})

    # Filter products based on 'using' field
    products = Products.objects.filter(using=forusing)

    # Pass filtered products to template as 'items'
    return render(request, 'categories.html', {"items": products})


def Signupform(request):
 
    fullname = request.POST.get('fullname')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirmpass = request.POST.get('confirmpass')

    if password != confirmpass :
        messages.error(request, "Passwords do not match!")
        return render(request,"signup.html",{"error":"Passwords do not match!"})

    if Signup.objects.filter(username=username).exists():
        messages.error(request, "Username already taken!")
        return render(request, "signup.html",{"error":"Username already taken"})

    if Signup.objects.filter(email=email).exists():
        messages.error(request, "Email already registered!")
        return render(request,"signup.html",{"error":"Email already registered!"})

    # Signup.objects.create(fullname=fullname, email=email, username=username, password=password, confirmpass=confirmpass)
    
    User.objects.create_user(email=email, username=username, password=password)

    messages.success(request, "Signup successful! Please log in.")
    return redirect("/login",{"error":"Signup successful! Please log in."})

    # return redirect('/signup')///////////////////

def Loginform(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    # more = Signup.objects.get(username=username)
    # print(more)

    # if(password == more.password) :
    #     request.session['userId'] = more.id
    #     return redirect("/main")
    # else :
    #     messages.error(request, "Invalid username or password")
    #     return render(request,"login.html",{"error":"Invalid username or password"})
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/main")
    # return re(request,"login.html") 

def Categories(request):

    categori = request.GET.get('categori')  

    view = Products.objects.filter(categori=categori)
    print(view)
     
    return render(request, 'categories.html', {"view": view})

def AddCart(request):

    productId = request.GET.get('id')
    type = request.GET.get('type')
    userId = request.session['userId']
    print(type)

    cart_item, created = Cart.objects.get_or_create(productId_id= productId, userId_id= userId, defaults={"quantity": 1})

    if not created:
        if type == "incre":
            cart_item.quantity += 1
        elif type == "decre":
            if cart_item.quantity == 1:
                removeId = request.GET.get('id')
                Cart.objects.filter(productId=removeId).delete()
                return redirect('/cart')    
            cart_item.quantity -= 1
        cart_item.save()

    return redirect("/cart")

def UserCart(request):

    userId = request.session.get('userId')  
    if not userId:
        return redirect("/login")  

    cart_items = Cart.objects.filter(userId_id=userId)  

    cartData = []
    subtotal = 0
    delivery_charge = 10  

    for item in cart_items:
        products = Products.objects.get(id=item.productId_id)
        item_subtotal = item.quantity * products.price
        subtotal += item_subtotal  

        cartData.append({
            "id": products.id,
            "product": products.product,
            "price": products.price,
            "image": products.image,
            "quantity": item.quantity,
            "subtotal": item_subtotal
        })

    total_price = subtotal + delivery_charge  
    
    return render(request, "cart.html", {"data": cartData, "subtotal": subtotal,"total_price": total_price})

def RemoveId(request):

    removeId = request.GET.get('id')
    print(removeId)
    Cart.objects.filter(productId=removeId).delete()
    
    return redirect('/cart')

def CheckOut(request):

    userId = request.session.get('userId')  
    cart_items = Cart.objects.filter(userId_id=userId)  

    cartData = []
    subtotal = 0
    delivery_charge = 10  

    for item in cart_items:
        products = Products.objects.get(id=item.productId_id)
        item_subtotal = item.quantity * products.price
        subtotal += item_subtotal  

        cartData.append({
            "quantity": item.quantity,
        })

    total_price = subtotal + delivery_charge  
    total_items = sum(item["quantity"] for item in cartData)  

    return render(request, "checkout.html", {"data": cartData,"total_items": total_items,"total_price":total_price})

def OrderID(request):

    fullname = request.POST.get('fullname')
    email = request.POST.get('email')
    phonenumber = request.POST.get('phonenumber')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    pincode = request.POST.get('pincode')
    paymentmethod = request.POST.get('paymentmethod')

    Order.objects.create(fullname=fullname, email=email, phonenumber=phonenumber, address=address, city=city, state=state, pincode=pincode, paymentmethod=paymentmethod)

    return redirect('/successful')

def SuccessFul(request):

    return render(request, "ordersuccess.html")

def ConTact(request):

    return render(request, "contact.html")

def ContactFrom(request):

    yourname = request.POST.get('yourname')
    youremail = request.POST.get('youremail')
    message = request.POST.get('message')

    Contact.objects.create(yourname=yourname, youremail=youremail, message=message)

    return redirect('/contact')
