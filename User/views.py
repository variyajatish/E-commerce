from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Products, Newlist, Featuredproducts, Category, Signup, Cart


def HomePage(request):
    return render(request,'Home.html')


def LoginPage(request):

    return render(request, 'login.html')


def SignupPage(request):
    return render(request, 'signup.html')


def MainPage(request):

    data = Products.objects.all()[:8]
    user = Newlist.objects.all()
    items = Featuredproducts.objects.all()
    view = Category.objects.all()

    return render(request, 'main.html', {"data":data, "user":user, "items":items, "view":view })


def ProductPage(request):

    viewId = request.GET.get('id')  

    data = Products.objects.get(id=viewId)
    print(data)

    return render(request, 'product.html', {"data": data})


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

    Signup.objects.create(fullname=fullname, email=email, username=username, password=password, confirmpass=confirmpass)
    
    messages.success(request, "Signup successful! Please log in.")
    return redirect("/login",{"error":"Signup successful! Please log in."})

    # return redirect('/signup')


def Loginform(request):

    username = request.POST.get('username')
    password = request.POST.get('password')

    more = Signup.objects.get(username=username)
    # print(more)

    if(password == more.password) :
        request.session['userId'] = more.id
        return redirect("/main")
    else :
        messages.error(request, "Invalid username or password")
        return render(request,"login.html",{"error":"Invalid username or password"})

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
    total_price = 10

    for item in cart_items:
        products = Products.objects.get(id=item.productId_id)
        subtotal = item.quantity * products.price
        total_price += subtotal

        cartData.append({
            "id": products.id,
            "product": products.product,
            "price": products.price,
            "image": products.image,
            "quantity": item.quantity,
            "subtotal": subtotal
        })

    return render(request, "cart.html",{"data":cartData, "total_price": total_price})

def RemoveId(request):

    removeId = request.GET.get('id')
    print(removeId)
    Cart.objects.filter(productId=removeId).delete()
    
    return redirect('/cart')
