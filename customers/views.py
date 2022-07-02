from cgi import test
from django.shortcuts import render
from customers.forms import NewCustomer, NewSoftware
from .models import Customers, Software

def customers(request):  
    if request.method == "POST":  
        form = NewCustomer(request.POST)  
        if form.is_valid():
            form.save()
            return render(request, 'customers/customer_list.html')
    else:  
        form = NewCustomer()  
    return render(request,'form.html',{'form':form})

def list_customers(request): 
    queryset = Customers.objects.all()
    context = {"object_list": queryset}
    return render(request, "customers/customer_list.html", context)

def delete_customers(request, pk):
    customer = Customers.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        return render(request, 'customers/customer_list.html')
    context = {'item':customer}
    return render(request, "customers/delete.html", context)

def edit_customer(request, pk):
    customer = Customers.objects.get(id=pk)
    form=NewCustomer(instance=customer)
    if request.method == "POST":  
        form = NewCustomer(request.POST, instance=customer)  
        if form.is_valid():
            form.save()
            return render(request, 'customers/customer_list.html')

    context = {'form':form}
    return render(request, "form.html", context)

def new_software(request, pk):  
    customer = Customers.objects.get(id=pk)
    form=NewSoftware(initial={'customer_pk':pk})
    if request.method == "POST":  
        form = NewSoftware(request.POST, request.FILES, initial={'customer_pk':pk})  
        if form.is_valid():
            form.save()
            return render(request, 'software/customersoftwarelist.html')
    else:  
        form = NewSoftware(initial={'customer_pk':pk})  
        
    return render(request,'software/newsoftware.html', {'form':form, 'item': customer})

def list_customer_software(request,pk):
    customer = Customers.objects.get(id=pk)
    queryset = Software.objects.filter(customer_pk=pk)
    context = {"object_list": queryset, 'item':customer}
    return render(request, "software/customersoftwarelist.html", context)

def listsoftware(request): 
    queryset = Software.objects.all()
    context = {"object_list": queryset}
    return render(request, "software/list.html", context)

def delete_software(request, pk):
    software = Software.objects.get(id=pk)
    if request.method == "POST":
        software.delete()
        return render(request, 'software/list.html')
    context = {'item':software}
    return render(request, "software/delete.html", context)

def edit_software(request, pk):
    software = Software.objects.get(id=pk)
    form=NewSoftware(instance=software)
    if request.method == "POST":  
        form = NewSoftware(request.POST, request.FILES, instance=software)  
        if form.is_valid():
            form.save()
            return render(request, 'software/list.html')

    context = {'form':form, 'item':software}
    return render(request, "software/editsoftware.html", context)  