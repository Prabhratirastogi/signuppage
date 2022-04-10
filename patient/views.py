from ast import Not
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Contact, Signup
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request,'patient/index.html')

def home(request):
    return render(request,'patient/home.html')

def about(request):
    return render(request,'patient/about.html')

# def signup(request):
#     if request.method == "POST"
#     return render(request,'doctor/signup.html')

# def signup(request):
#     if request.method == "POST":
#         #get the the post para meters
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         username = request.POST['username']
#         email = request.POST['email']
#         address = request.POST['address']
#         image = request.POST['image']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']

#         myuser = User.objects.create_user(username,email,pass1)
#         myuser.first_name = fname
#         myuser.last_name = lname
#         myuser.save()
#         messages.success(request, "Your account has been successfully created")
#         return redirect('login')

#     else:
#         return render(request, 'doctor/signup.html')

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        add = request.POST['address']
        image = request.POST['profile_photo']  #leftside id name right side name
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.address = add
        myuser.Profile_Photo = image
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        signupps = Signup(first_name=fname, last_name=lname,username=username,email=email, address = add, img=image, passs1=pass1, pass2=pass2)
        #left side name from models right side id from signup.html
        # print(myuser)
        signupps.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        return redirect('home')
    else:
        return render(request,'patient/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, pass1=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "patient/logout.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "patient/login.html")

        

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         pass1 = request.POST['pass1']
        
#         if username==Signup(username) and pass1 == Signup(pass1):
#             return redirect('logout')
#         else:
#             messages.error(request, "Bad Credentials!!")
#             return redirect('home')

        
        # if myuser is  None:
        #     messages.error(request, "Bad Credentials!!")
        #     return redirect('home')
        # if myuser is not None:

        #     return render(request,'logout.html')
    
    # return render(request, "doctor/login.html")

def logout(request):
    logout(request)
    messages.success(request,'Successfully Logged Out')
    return redirect('home')
   



def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact_user = Contact(name=name, email=email, phone=phone, desc=desc)
        contact_user.save()
    return render(request, 'patient/contact.html')