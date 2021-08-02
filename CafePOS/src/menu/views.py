from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import datetime

from .models import Menu, Category, Size
from .forms import CategoryForm, MenuForm


# Create your views here.
""" block category """
def menu_category_list(request):
    queryset = Category.objects.filter(is_deleted=False)
    template_name = 'menu/list_category.html'
    context = {
        'title': "Customer",
        'list': queryset,
    }
    return render(request, template_name, context)


def menu_category_add(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.creator = request.user
        instance.created = datetime.datetime.now()
        instance.save()
        messages.success(request, 'Customer Added Successfull.!')
        return redirect(f'/menu/category')

    template_name = 'menu/form_category.html'
    context = {
        'title': "Add Category  ",
        'form': form
    }
    return render(request, template_name, context)


def menu_category_edit(request, id):
    instance = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.updater = request.user
            form.updated = datetime.datetime.now()
            form.save()
            messages.success(request, 'Category Updated Successfull.!')
            return redirect(f"/menu/category")

    template_name = 'menu/form_category.html'
    context = {
        "title": "Edit Category",
        "form": form,
    }
    return render(request, template_name, context)


def menu_category_delete(request, id):
    instance = get_object_or_404(Category, id=id)

    template_name = 'menu/delete.html'
    if request.method == "POST":
        instance.deleter = request.user
        instance.deleted = datetime.datetime.now()
        instance.is_deleted = True
        instance.save()
        messages.success(request, 'Category Deleted Successfull.!')
        return redirect("/menu/category")

    context = {
        "title": "Delete",
        "instance": instance
    }
    return render(request, template_name, context)


""" endblock category """
""" block menu """


def menu_list(request):
    queryset = Menu.objects.filter(is_deleted=False)
    template_name = 'menu/list_menu.html'
    context = {
        'title': "Menu",
        'list': queryset,
    }
    return render(request, template_name, context)


def menu_add(request):
    form = MenuForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.creator = request.user
        instance.created = datetime.datetime.now()
        instance.save()
        messages.success(request, 'Customer Added Successfull.!')
        return redirect(f'/menu')

    template_name = 'menu/form_menu.html'
    context = {
        'title': "Add Menu  ",
        'form': form
    }
    return render(request, template_name, context)


def menu_edit(request, id):
    instance = get_object_or_404(Menu, id=id)
    form = MenuForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.updater = request.user
            form.updated = datetime.datetime.now()
            form.save()
            messages.success(request, 'Menu Updated Successfull.!')
            return redirect(f"/menu")

    template_name = 'menu/form_menu.html'
    context = {
        "title": "Edit Menu",
        "form": form,
    }
    return render(request, template_name, context)


def menu_delete(request, id):
    instance = get_object_or_404(Menu, id=id)

    template_name = 'menu/delete.html'
    if request.method == "POST":
        instance.deleter = request.user
        instance.deleted = datetime.datetime.now()
        instance.is_deleted = True
        instance.save()
        messages.success(request, 'Menu Deleted Successfull.!')
        return redirect("/menu")

    context = {
        "title": "Delete",
        "instance": instance
    }
    return render(request, template_name, context)


""" endblock menu """



def get_menu_dd(request):
    id_category = request.POST.get('id_category') or 0
    obj_list = Menu.objects.filter(category_id=id_category, category__is_deleted=False, is_deleted=False).values_list('id','name')
    response = {
        'obj_list':list(obj_list)
    }
    return JsonResponse(response)


def get_size_dd(request):
    id_category = request.POST.get('id_category') or 0
    obj_list = Size.objects.filter(category_id=id_category, category__is_deleted=False, is_deleted=False).values_list('id','size')
    response = {
        'obj_list':list(obj_list)
    }
    return JsonResponse(response)
