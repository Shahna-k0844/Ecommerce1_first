from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from.models import *
from .forms import CategoryForm, productsForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def homefunction(request):
    product=products.objects.all()
    Category=categories.objects.all()
    both={
        'product':product,
        'category':Category
    }

    # for i in product:
    #     print(product)
    return render(request,'home.html',both)
def productfunction(request,id=id):
    product=products.objects.all()
    return render(request,'product.html',{'product':product})
def categoryfunction(request):
    Category=categories.objects.all()
    return render(request,'categories.html',{'category':Category})
def cat_products(request,id):
    product=products.objects.filter(Category__id=id)
    return render(request,'cat_prod.html',{'cat_prod':product})
def view_products(request,id):
    product=products.objects.get(id=id)
    return render(request,'view_prod.html',{'viewprod':product})

def cartfunction(request,id):
    
    if request.user.is_authenticated:
        product=products.objects.get(id=id)
        user=request.user
        price=product.rate 
        cartitems=Cart.objects.filter(user=user,product=product).first()
        if cartitems:
            cartitems.quantity+=1
            cartitems.price*=2
            cartitems.save()

            
            # messages.error(request,"item already exist in the cart")
            
        else:

            item=Cart.objects.create(user=user,product=product,quantity=1,price=price)

        # if item is not None :
        #     messages.warning(request,"item already exist in the cart")


        # total_each=(item.quantity * item.product.rate)
        # print(total_each)
        # return render(request,'cartfinal.html',{'total_each':total_each})

    
        return redirect('cartpage')

        # def totalprice(self):
        #     price=(self.product.rate)*(self.product.quantity)
        #     return price

        
    else:
        return render(request,'login.html')
def cartpage(request):
    if request.user.is_authenticated:
        cartitems=Cart.objects.filter(user=request.user)
        # if not cartitems:
        #     cartitems.quantity+=1
        #     cartitems.save()
        total=sum(item.quantity * item.product.rate for item in cartitems)
        number=0
        if cartitems:
        #     number+=1
        # print(number)
            # for item in cartitems:
            #     quantity=item.quantity
            quantity=sum(item.quantity for item in cartitems)
        quantity=sum(item.quantity for item in cartitems)

                
        return render(request,'cartfinal.html',{'cartprod':cartitems,'total':total,'quantity':quantity})
    else:
        return render(request,'login.html')
# def morethanone(request,id):
    
        
        
        
    # return render(request,'cart.html')
def removefunction(request,id):
    if request.user.is_authenticated:
        cart_items=Cart.objects.get(id=id,user=request.user)
        cart_items.delete()
        return redirect('cartpage')
    else:
        return render(request,'login.html')

def wishfunction(request, id):
    if request.user.is_authenticated:
        product = products.objects.get(id=id)
        user = request.user
        wishitems = Wishlist.objects.filter(user=user, product=product).first()
        
        if wishitems:
            messages.error(request, "Item already exists in the wishlist")
            return redirect('home')
        else:
            Wishlist.objects.create(user=user, product=product)
            messages.success(request, "Product added to wishlist")
            return redirect('wishpage')
    else:
        return redirect('login')

def wishpage(request):
    if request.user.is_authenticated:
        wishitems = Wishlist.objects.filter(user=request.user)
        return render(request, 'wishlist.html', {'wishlist': wishitems})
    else:
        return redirect('login')
# def placeorderfunction(request):
#     cart_items=Cart.objects.filter(user=request.user)
#     if not cart_items.exists():
#         return redirect('products')
#     # else:
#     orderexists=Order.objects.filter(user=request.user).first()
#     total=sum(item.quantity * item.product.rate for item in cart_items)

#     if request.method =='POST' :
#         address=request.POST['address']
#         if orderexists:
#             orderexists.address=address
#             orderexists.save()
#         else:
#             order=Order.objects.create(user=request.user,address=address)  
#         cart_items.delete() 
#         return redirect('order')
#     return render(request,'place_order.html',{'cartitems':cart_items,'total':total,'user':request.user,'existingaddres':orderexists.address if orderexists else '' })    
def placeorderfunction(request):
    cartitems=Cart.objects.filter(user=request.user)
    if not cartitems.exists():
        return redirect('products')
    
    exist_order=Order.objects.filter(user=request.user).first()
    total=sum(item.quantity * item.product.rate for item in cartitems)

    if request.method=='POST':
        address=request.POST['address']
        if exist_order:
            exist_order.address=address
            exist_order.save()
        else:
            orders=Order.objects.create(user=request.user,address=address)
        cartitems.delete()
        return redirect('thankyou')
    return render(request,'place_order.html',{'cartitems':cartitems,'total':total,'user':request.user,'exist_address':exist_order.address if exist_order else ''})          
def orderconfirmfunction(request):
    return render(request,'thankyou.html')

def signfunction(request):
    if request.method == 'POST':
        Name=request.POST.get('name') # either use .get or POST['.....']
        username=request.POST['email']
        email=request.POST['email']
        password=request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()


        # print(Name,Email,Password)
    return render(request,'sign_up.html')
def loginfunction(request):
    if request.method == 'POST':
        username=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return render(request,'adminhome.html')
            else:
                return redirect('home')
        else:
            messages.error(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')
def logoutfunction(request):
    logout(request)
    return redirect('home')

# form methode(creating products and category)
def createcategory(request):
    if request.method=='POST':
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"category is created")
            return redirect('home')
    else:
        form=CategoryForm()
      
        
    return render(request,'categoryform.html',{'form':form})

def createproduct(request):
    if request.method=='POST':
        form=productsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request,"category is created")
            return redirect('home')

    else:
        form=productsForm()
    return render(request,'productform.html',{'form':form})
def adminsite(request):
     return render(request,'adminhome.html')
def viewcreatedProd(request):
    product=products.objects.all()
    return render(request,'createdproductview.html',{'product':product})
def viewcreatedCat(request):
    Category=categories.objects.all()
    return render(request,'createdcategoryview.html',{'Category':Category})
def deletebysuper(request,id):
    product=products.objects.get(id=id)
    product.delete()
    return redirect('viewcreatedProd')
def editbysuper(request,id):
    edit=products.objects.get(id=id)
    form=productsForm(request.POST,request.FILES)

    if request.method=='POST':
        if 'image' in request.FILES:
            image=request.FILES['image']
        
        # image=request.POST['image']
        name=request.POST['name']
        description=request.POST['description']
        rate=request.POST['rate']
        if edit:
            edit.image=image
            edit.name=name
            edit.description=description
            edit.rate=rate
            edit.save()
            return redirect('viewcreatedProd')
        else:
            form=productsForm
    return render(request,'editproduct.html',{'form':form,'edit':edit})
        