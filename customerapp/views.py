from django.shortcuts import render,redirect
from django.contrib import messages
from adminapp.models import Product
from mainapp.models import Customer
from .models import Response

# Create your views here.

def customerdash(request):
    if not 'customerid' in request.session:
        messages.error(request,'Login First')
        return redirect('login')
    customerid = request.session['customerid']
    context = {
        'customerid':customerid
    }
    return render(request,'customerdash.html',context)

def customerlogout(request):
    try:
        del request.session['customerid']
        messages.success(request,'Logged Out')
        return redirect('login')
    except:
        messages.error(request,'Error')
        return redirect('login')
def customerproducts(request):
    if not 'customerid' in request.session:
        messages.error(request,'Login First')
        return redirect('login')
    customerid = request.session['customerid']
    products = Product.objects.all()
    context ={
        'customer':customerid,
        'products':products,
    }
    
    return render(request,'customerproduct.html',context)
 

def viewprofile(request):
    if not 'customerid' in request.session:
        messages.error(request,'Login First')
        return redirect('login')
    customerid = request.session['customerid']
    customer = Customer.objects.get(email=customerid)
    context = {
        'customerid':customerid,
        'customer':customer

    }
    return render(request,'viewprofile.html',context)

def updateprofile(request):
    if not 'customerid' in request.session:
        messages.error(request,'Login First')
        return redirect('login')
    customerid = request.session['customerid']
    customer = Customer.objects.get(email=customerid)
    if request.method =='POST':
        customer.name = request.POST.get('name')
        customer.contactno = request.POST.get('contactno')
        customer.gender = request.POST.get('gender')
        customer.address = request.POST.get('address')
        if request.FILES.get('picture'):
            customer.picture = request.FILES.get('picture')
        customer.save()
        messages.success(request,'profile Updated')
        return redirect('viewprofile')
    context = {
        'customerid':customerid,
        'customer':customer

    }
    return render(request,'updateprofile.html',context)


def submitresponse(request):
    if not 'customerid' in request.session:
        messages.error(request,'Login First')
        return redirect('login')
    customerid = request.session['customerid']
    customer =Customer.objects.get(email=customerid)
    if request.method =='POST':
       responsetype=request.POST.get('responsetype')
       responsetext=request.POST.get('responsetext')
       res = Response(user=customer,responsetype=responsetype,responsetext=responsetext)
       res.save()
       if responsetext =='feedback':
           messages.success(request,'feedback Submitted')
       else:
           messages.success(request,'Complaint Submitted')
       return redirect('submitresponse')
    context = {
        'customerid':customerid
    }
    return render(request,'submitresponse.html',context)
