from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Product
from customerapp.models import Response
# Create your views here.

def admindash(request):
    if not 'adminid' in request.session:
        messages.error(request,"login first")
        return redirect('login')
    adminid = request.session['adminid']
    context = {
        'adminid':adminid
    }
    return render(request,'admindash.html',context)

def adminlogout(request):
    if not 'adminid' in request.session:
        del request.session['adminid']
        messages.success(request,"Logged out successfully")
        return redirect('login')
    else:
        messages.error(request,"Something went wrong")
        return redirect('login')
    
def viewenq(request):
    if not 'adminid' in request.session:
        messages.error(request,"login first")
        return redirect('login')
    adminid = request.session['adminid']
    context = {
        'adminid':adminid
    }
    return render(request,'viewenq.html',context)

def addproduct(request):
    if not 'adminid' in request.session:
        messages.error(request,"login first")
        return redirect('login')
    if request.method =="POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        price=request.POST.get('price')
        mfgdate=request.POST.get('mfgdate')
        expdate=request.POST.get('expdate')
        picture=request.FILES.get('picture')
        pro =Product(name=name,description=description,price=price,mfgdate=mfgdate,expdate=expdate,picture=picture)
        pro.save()
        messages.success(request,"product Added Succesfully")
        return redirect("viewproduct")
    adminid = request.session['adminid']
    context = {
        'adminid':adminid
    }
    return render(request,'addproduct.html',context)

def viewproduct(request):
    if not 'adminid' in request.session:
        messages.error(request,"login first")
        return redirect('login')
    adminid = request.session['adminid']
    products =Product.objects.all()
    context = {
        'adminid':adminid,
        'products':products
    }
    return render(request,'viewproduct.html',context)


def delproduct(request,pid):
    if not 'adminid' in request.session:
        messages.error(request,"login first")
        return redirect('login')
    Product.objects.get(pid=pid).delete()
    messages.success(request,"Product Deleted Sucessfully ")
    return redirect('viewproduct')

def viewfeedbacks(request):
    if not 'adminid' in request.session:
        messages.error(request,"login first")
        return redirect('login')
    adminid = request.session['adminid']
    feedbacks =Response.objects.filter(responsetype='feedback')
    context = {
        'adminid':adminid,
        'feedbacks':feedbacks
    }
    return render(request,'viewfeedback.html',context)

def viewcomplaints(request):
    if not 'adminid' in request.session:
        messages.error(request,"login first")
        return redirect('login')
    adminid = request.session['adminid']
    complaints =Response.objects.filter(responsetype='complaint')
    context = {
        'adminid':adminid,
        'complaints':complaints
    }
    return render(request,'viewcomplaints.html',context)

def delcomplaints(request,id):
    Response.objects.get(id=id).delete()
    messages.success(request,'Complaint Deleted Succesfully')
    return redirect('admindash')


def delfeedbacks(request,id):
    Response.objects.get(id=id).delete()
    messages.success(request,'Feedback Deleted Succesfully')
    return redirect('admindash')
