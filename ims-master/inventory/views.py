from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse

from .models import *
from .forms import *


def index(request):
    products = Product.objects.all()
    context = {'products': products, 'flag': 'product'}
    return render(request, 'inventory/index.html', context)


def windows(request):
    products = Windows.objects.all()
    context = {'products': products, 'header': 'Displaying Windows Inventory', 'flag': 'windows'}
    return render(request, 'inventory/index.html', context)


def linux(request):
    products = Linux.objects.all()
    context = {'products': products, 'header': 'Displaying Linux Inventory', 'flag': 'linux'}
    return render(request, 'inventory/index.html', context)


def network(request):
    products = Network.objects.all()
    context = {'products': products, 'header': 'Displaying Network Inventory', 'flag': 'network'}
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
        form = LinuxForm()
    return render(request, 'inventory/new.html', {'form': form})


def addnew_linux(request):
    display_name = "ADDING A NEW ENTRY TO LINUX INVENTORY"
    if request.method == 'POST':
        form = LinuxForm(request.POST)
        print(dir(form))
        if form.is_valid():
            # product = form.save(commit=True)
            form.save()
            return redirect('index')
    else:
        form = LinuxForm()
    return render(request, 'inventory/new.html', {'form': form, 'display_name': display_name})


def addnew_windows(request):
    display_name = "ADDING A NEW ENTRY TO WINDOWS INVENTORY"
    if request.method == 'POST':
        form = WindowsForm(request.POST)
        print(dir(form))
        if form.is_valid():
            # product = form.save(commit=True)
            form.save()
            return redirect('index')
    else:
        form = WindowsForm()
    return render(request, 'inventory/new.html', {'form': form, 'display_name': display_name})


def addnew_network(request):
    display_name = "ADDING A NEW ENTRY TO NETWORK INVENTORY"
    if request.method == 'POST':
        form = NetworkForm(request.POST)
        print(dir(form))
        if form.is_valid():
            # product = form.save(commit=True)
            form.save()
            return redirect('index')
    else:
        form = NetworkForm()
    return render(request, 'inventory/new.html', {'form': form, 'display_name': display_name})


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


# def delete(request, pk):
#     template = 'inventory/index.html'
#     item = get_object_or_404(Product, pk=pk)
#     try:
#         if request.method == 'POST':
#             form = ProductForm(request.POST, instance=item)
#             if form.is_valid():
#                 form.save()
#                 return redirect('index')
#             item.delete()
#             messages.success(request, "Successfully deleted")
#         else:
#             form = ProductForm(instance=item)
#     except Exception as e:
#         messages.warning(request, "NOT DELETED")
#
#     items = Product.objects.all()
#
#     context = {
#         'products': items,
#     }
#
#     return render(request, template, context)
#

def delete(request, pk, header):

    if header == 'linux':
        cls = Linux
    elif header == 'windows':
        cls = Windows
    else:
        cls = Network

    template = 'inventory/index.html'
    cls.objects.filter(id=pk).delete()

    items = cls.objects.all()

    context = {
        'products': items,
    }

    print(header)

    return render(request, template, context)
