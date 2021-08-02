from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from customer.models import Customer
from order.models import Order



# Create your views here.

@login_required(login_url='accounts/login')
def home(request):
    staff = User.objects.count() or 0
    customers = Customer.objects.count() or 0
    service = Order.objects.filter(ordertype='service').count() or 0
    takeaway = Order.objects.filter(ordertype='takeaway').count() or 0
    delivery = Order.objects.filter(ordertype='delivery').count() or 0

    template_name = 'home/home.html'
    context = {
        'title': "Home",
        'customers':customers,
        'staff':staff,
        'service':service,
        'takeaway':takeaway,
        'delivery':delivery
    }
    return render(request, template_name, context)

