from django.shortcuts import render,redirect
from.models import LoginInfo,Customer
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        contactno = request.POST.get('contactno')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')
        user = LoginInfo.objects.filter(username=email).first()
        if user:
            messages.error(request,"Email already exists")
            return redirect('register')
        log = LoginInfo(usertype ="customer",username = email,password=password)
        cust = Customer(login=log,name=name,gender=gender,contactno=contactno,email=email,address=address)
        log.save()
        cust.save()
        messages.success(request, 'Registration Successfull')
        return redirect('login')
    return render(request,'register.html')
def login(request):
    if request.method=="POST":
        username =request.POST.get('username')
        password =request.POST.get('password')
        try:
            user =LoginInfo.objects.get(username=username,password=password)
            if user:
                if user.usertype=="admin":
                    request.session['adminid'] = username
                    messages.success(request,"Welcome admin")
                    return redirect('admindash')
                elif user.usertype=="customer":
                    request.session['customerid'] =username
                    messages.success(request,"login successfull")
                    return redirect('customerdash')
        except LoginInfo.DoesNotExist:
            messages.error(request,"Wrong username or password")
            return redirect('login')    
    return render(request,'login.html')
