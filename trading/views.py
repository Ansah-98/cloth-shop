from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Profile,Product,Comment
from .forms import ProductForm
from django.db.models import Q
from .no_repititions import Onlyone
# Create your views here

def home(request):

    q = request.GET.get('q')
    if q is None:
        product = Product.objects.all()
        print(type(product))
    else:
        product = Product.objects.filter(Q(name__icontains =q)|
        Q(type_of__icontains=q)|
        Q(brand__icontains = q)|
        Q(by__user__username__icontains =q))
     
    context = { 'product' : product ,'obj':'obj',}
    return render(request,'trading/index.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username= username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        
    return render(request,'trading/loginPage.html')

def signOut(request):
    user = request.user
    if user == None:
        return redirect('home')
    logout(request)
    return redirect('login')


def createUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['c-password']
        if password != con_password:
            messages.error(request,'confirmed password does not match password')
            
        user = User.objects.filter(username =username).first() or User.objects.filter(email =email).first()

        if user is not None:
            messages.error(request,'user already exist check email or uusername')
        user = User.objects.create_user(username =username,email=email, password =password)
        login(request, user )
        return redirect('profile-CU')
    return render(request,'trading/register.html',)
def createProfile(request):
    if request.user.is_authenticated == False:
        return redirect('home')
    profile = Profile.objects.filter(user=request.user).first()

    if request.method == 'POST':
    
        if profile != None :
            profile.location= request.POST['location']
            profile.bio =request.POST['bio']
            profile.number = request.POST['number']
            
            profile.save()
            return redirect('home')
        else:
            location = request.POST['location']
            bio = request.POST['bio']
            number = request.POST['number']
            new_prof = Profile.objects.create(user =request.user, location =location,bio =bio, number = number)
            new_prof.save()
            return redirect('home')
    return render(request,'trading/createProfile.html', {'profile': profile} )
#@login_required(login_url ='login')
def postProduct(request):
    if request.user.is_authenticated != True:
        return redirect('home')
    profile = Profile.objects.get( user = request.user)  
    form = ProductForm()

    if profile is None:
        return redirect('profile-CU')
    if request.method == 'POST':
        name = request.POST['name']
        brand = request.POST['brand']
        price =request.POST['price']
        type_of = request.POST['type_of']
        new_pro = Product.objects.create(by = profile , 
        name = name ,
         brand = brand, 
         price = price, 
         type_of =type_of )
        new_pro.save()
        return redirect('home')
    return render(request,'trading/new_product.html',{'form':form})

def profile_page(request,pk):
    profile = Profile.objects.get(pk=pk)
    product = Product.objects.filter(by = profile)
    print(product)
    context = {'profile':profile,'products':product}
    return render(request, 'trading/profile.html',context)