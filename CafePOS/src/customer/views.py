import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Customer
from .forms import CustomerForm
from order.models import Order


# Create your views here.
def customer_list(request):
    queryset = Customer.objects.filter(is_deleted=False)
    template_name = 'customer/list.html'
    context = {
        'title': "Customer",
        'list': queryset,
    }
    return render(request, template_name, context)


# showing customer profile
def customer_profile(request, id):
    profile = Customer.objects.get(id=id)
    orders = Order.objects.filter(customer=profile).count()

    template_name = 'customer/profile.html'
    context = {
        'title': "Customer",
        'profile': profile,
        'orders': orders
    }
    return render(request, template_name, context)


def customer_add(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.creator = request.user
        instance.created = datetime.datetime.now()
        instance.save()
        messages.success(request, 'Customer Added Successfull.!')
        return redirect(f'/customer/{instance.id}/profile')

    template_name = 'customer/form.html'
    context = {
        'title': "Customer",
        'form': form
    }
    return render(request, template_name, context)


def customer_edit(request, id):
    instance = get_object_or_404(Customer, id=id)
    form = CustomerForm(request.POST or None, request.FILES or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.updater = request.user
            form.updated = datetime.datetime.now()
            form.save()
            messages.success(request, 'Customer Updated Successfull.!')
            return redirect(f"/customer/{id}/profile")

    template_name = 'customer/form.html'
    context = {
        "title": "Edit",
        "form": form,
    }
    return render(request, template_name, context)


def customer_delete(request, id):
    instance = get_object_or_404(Customer, id=id)

    template_name = 'customer/delete.html'
    if request.method == "POST":
        instance.deleter = request.user
        instance.deleted = datetime.datetime.now()
        instance.is_deleted = True
        instance.save()
        messages.success(request, 'Customer Deleted Successfull.!')
        return redirect("/customer")

    context = {
        "title": "Delete",
        "instance": instance
    }
    return render(request, template_name, context)