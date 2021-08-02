from django.db.models import Sum
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import generics

from .forms import OrderForm
from .models import  Order, TempOrderItem, OrderItem, Table
from .serializers import TempOrderItemListSerializer
from menu.models import Menu, Price
from customer.models import Customer
from customer.forms import CustomerForm

import datetime


# Create your views here.
def order_list(request):
    queryset = Order.objects.filter(is_deleted=False)

    template_name = 'order/list.html'
    context = {
        'title': "Order",
        'list': queryset,
    }
    return render(request, template_name, context)


# order service
def order_service_table(request):
    queryset = Table.objects.filter(is_deleted=False)

    template_name = 'order/service_table.html'
    context = {
        'title': "Table",
        'list': queryset,
    }

    return render(request, template_name, context)


def order_service_customer(request, id_table):
    form = CustomerForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid:
            name = request.POST['name'] or None
            mobile = request.POST['mobile'] or '00000000000'
            address = request.POST['address'] or None

            obj, created = Customer.objects.get_or_create(mobile=mobile)
            if created:
                obj.name = name
                obj.address = address
            obj.save()

            order = Order.objects.create(
                ordertype='service', customer=obj,
                creator=request.user, created=datetime.datetime.now()
            )

            table = Table.objects.get(id=id_table)
            table.order = order
            table.is_reserved = True
            table.save()

            order.table_number = table.number
            order.save()

            return redirect(f'/order/{order.id}/service')

    template_name = 'order/form_customer.html'
    context = {
        'title': "Service",
        'form': form,
    }
    return render(request, template_name, context)


def order_service(request, id):
    form = OrderForm(request.POST or None)

    template_name = 'order/form_service.html'
    context = {
        'title': "Service",
        'form': form,
        'id_order':id
    }
    return render(request, template_name, context)


# order take away
def order_takeaway_customer(request):
    form = CustomerForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid:
            name = request.POST['name'] or None
            mobile = request.POST['mobile'] or '00000000000'
            address = request.POST['address'] or None

            obj, created = Customer.objects.get_or_create(mobile=mobile)
            if created:
                obj.name = name
                obj.address = address
            obj.save()

            order = Order.objects.create(
                ordertype='takeaway', customer=obj,
                creator=request.user, created=datetime.datetime.now()
            )

            return redirect(f'/order/{order.id}/takeaway')

    template_name = 'order/form_customer.html'
    context = {
        'title': "Take Away",
        'form': form,
    }
    return render(request, template_name, context)


def order_takeaway(request, id):
    form = OrderForm(request.POST or None)

    template_name = 'order/form_takeaway.html'
    context = {
        'title': "Take Away",
        'form': form,
        'id_order':id
    }
    return render(request, template_name, context)


# order delivery
def order_delivery_customer(request):
    form = CustomerForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid:
            name = request.POST['name'] or 'Running'
            mobile = request.POST['mobile'] or '00000000000'
            address = request.POST['address'] or 'Bahawalnagar'

            obj, created = Customer.objects.get_or_create(mobile=mobile)
            obj.name = name
            obj.address = address
            obj.save()

            order = Order.objects.create(
                ordertype='delivery', customer=obj,
                creator=request.user, created=datetime.datetime.now()
            )

            return redirect(f'/order/{order.id}/delivery')

    template_name = 'order/form_customer.html'
    context = {
        'title': "Delivery Customer",
        'form': form,
    }
    return render(request, template_name, context)


def order_delivery(request, id):
    form = OrderForm(request.POST or None)

    template_name = 'order/form_delivery.html'
    context = {
        'title': "Delivery",
        'form': form,
        'id_order':id
    }
    return render(request, template_name, context)


class TableOrderItemListSerializerView(generics.ListAPIView):
    serializer_class = TempOrderItemListSerializer

    def get_queryset(self):
        id_order = self.request.GET.get('id_order') or None
        return TempOrderItem.objects.filter(order_id=id_order)


def add_temp_order_item(request):
    id_order = request.POST.get('id_order')
    id_category = request.POST.get('id_category')
    id_menu = request.POST.get('id_menu')
    id_size = request.POST.get('id_size')
    quantity = request.POST.get('quantity')

    # price = Menu.objects.filter(category_id=id_category, id=id_menu).values('price')[0]['price'] or 0
    price = Price.objects.filter(size_id=id_size, menu_id=id_menu).values('price')[0]['price'] or 0

    total = int(price) * int(quantity)

    obj = TempOrderItem()
    obj.order_id = id_order
    obj.category_id = id_category
    obj.menu_id = id_menu
    obj.size_id = id_size
    obj.quantity = quantity
    obj.total = total
    obj.status = 'waiting'
    obj.creator = request.user
    obj.created = datetime.datetime.now()
    obj.save()

    return JsonResponse({'success':True})


def remove_temp_order_item(request):
    id = request.POST['id'] or None
    TempOrderItem.objects.get(id=id).delete()
    return JsonResponse({'success':True})


def commit_temp_order_items(request):
    id_order = request.POST['id_order'] or None #order_id
    TempOrderItem.objects.filter(order_id=id_order).update(commit=True)
    return JsonResponse({'success':True})


def order_complete(request, id): # order Id
    temp_items = TempOrderItem.objects.filter(order_id=id)

    order_obj = Order.objects.get(id=id)
    order_obj.complete = True
    order_obj.save()

    if order_obj.ordertype == 'service':
        table = Table.objects.get(order=order_obj)
        table.is_reserved = False
        table.save()


    for temp_item in temp_items:
        item, created = OrderItem.objects.get_or_create(
            order=order_obj,
            category=temp_item.category,
            menu=temp_item.menu,
            size=temp_item.size,
        )
        item.quantity += temp_item.quantity
        item.total += temp_item.total
        item.creator = request.user
        item.created = datetime.datetime.now()
        item.save()

    temp_items.delete()

    return redirect(f'/order/{order_obj.id}/invoice')


def order_invoice(request, id):
    order = Order.objects.get(id=id, is_deleted=False)
    queryset = OrderItem.objects.filter(order=order, is_deleted=False)
    total_bill = queryset.aggregate(Sum('total'))['total__sum']

    template_name = 'order/invoice.html'
    context = {
        'title': "Invoice",
        'list':queryset,
        'total_bill': total_bill,
        'order': order,
    }
    return render(request, template_name, context)

