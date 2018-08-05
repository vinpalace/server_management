from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from .models import *
from .forms import ProductForm


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'inventory/index.html', context)

def windows(request):
    products = Windows.objects.all()
    context = {'products': products, 'header' : 'Displaying Windows Inventory'}
    return render(request, 'inventory/index.html', context)

def linux(request):
    products = Linux.objects.all()
    context = {'products': products, 'header' : 'Displaying Linux Inventory'}
    return render(request, 'inventory/index.html', context)

def network(request):
    products = Network.objects.all()
    context = {'products': products, 'header' : 'Displaying Network Inventory'}
    return render(request, 'inventory/index.html', context)



def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/detail.html', {'product': product})


def addnew(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        print(dir(form))
        if form.is_valid():
            # product = form.save(commit=True)
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'inventory/new.html', {'form': form})


def edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/edit.html', {'form': form})


#