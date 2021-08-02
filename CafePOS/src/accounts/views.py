import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from .tokens import account_activation_token
from .forms import RegisterationForm, UserProfileForm
from .models import UserProfile


# Create your views here.
@login_required(login_url='login')
def register(request):
    if not request.user.userprofile.roll == 'Admin':
        raise Http404

    if request.method == 'POST':
        is_active = request.POST.get('is_active') or False

        if is_active == 'on':
            is_active = True

        register_form = RegisterationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.is_active = is_active
            user.save()
            messages.success(request, 'Account Added Successfull.!')
            return HttpResponseRedirect(f'/accounts/{user.id}/profile/add')

    else:
        register_form = RegisterationForm()

    template_name = 'accounts/register_form.html'
    context = {
        'register_form': register_form
    }
    return render(request, template_name, context)


@login_required(login_url='login')
def accounts_add_profile(request, id):
    if not request.user.userprofile.roll == 'Admin':
        raise Http404

    if request.method == 'POST':
        userprofile_form = UserProfileForm(request.POST)

        if userprofile_form.is_valid():
            userprofile = userprofile_form.save(commit=False)
            userprofile.user_id = id
            userprofile.creator = request.user
            userprofile.created = datetime.datetime.now()
            userprofile.save()
            messages.success(request, 'Account Profile Added Successfull.!')
            return HttpResponseRedirect(f'/accounts/{userprofile.id}/profile')

    else:
        userprofile_form = UserProfileForm()

    template_name = 'accounts/profile_form.html'
    context = {
        'userprofile_form': userprofile_form
    }
    return render(request, template_name, context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home:home')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        template_name = 'registration/account_activation_invalid.html'
        context = {
            'title': 'Invalid'
        }
        return render(request, template_name, context)


@login_required(login_url='login')
def accounts_list(request):
    userprofile_list = UserProfile.objects.filter(is_deleted=False)

    template_name = 'accounts/list.html'
    context = {
        'title': 'Users',
        'userprofile_list': userprofile_list
    }
    return render(request, template_name, context)


@login_required(login_url='login')
def accounts_profile(request, id):
    instance = UserProfile.objects.get(id=id)

    template_name = 'accounts/profile.html'
    context = {
        'title': 'Profile',
        'profile': instance
    }
    return render(request, template_name, context)


@login_required(login_url='login')
def accounts_edit(request, id): # here is profile id..
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.userprofile.roll == 'Admin':
        raise Http404

    instance = get_object_or_404(UserProfile, id=id)
    userprofile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=instance)
    if request.method == 'POST':
        if userprofile_form.is_valid():
            userprofile_form.updater = request.user
            userprofile_form.updated = datetime.datetime.now()
            userprofile_form.save()
            messages.success(request, 'Profile Updated Successfull.!')
            return redirect(f"/accounts/{id}/profile")

    template_name = 'accounts/profile_form.html'
    context = {
        'title': 'Registeration',
        'userprofile_form':userprofile_form
    }
    return render(request, template_name, context)


@login_required(login_url='login')
def accounts_delete(request, id): # profile id
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.userprofile.roll == 'Admin':
        raise Http404

    instance = get_object_or_404(UserProfile, id=id)

    template_name = 'accounts/delete.html'
    if request.method == "POST":
        Users = get_user_model()
        user = get_object_or_404(Users, id=instance.user.id)
        user.is_active = False
        user.save()
        instance.deleter = request.user
        instance.deleted = datetime.datetime.now()
        instance.is_deleted = True
        instance.save()

        messages.info(request, 'Account Deleted Successfull.!')
        return redirect("/accounts")

    context = {
        "title": "Delete",
        "instance": instance
    }
    return render(request, template_name, context)