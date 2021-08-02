from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    is_active = forms.BooleanField(widget=forms.CheckboxInput, required=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder':'Enter Username'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder':'Enter Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder':'Enter Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder':'Enter Password', 'value':'User@1234'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder':'Re Enter Password', 'value':'User@1234'})
        self.fields['is_active'].widget.attrs.update({'class': 'form-check-input'})


    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'is_active', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cnic'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter CNIC'})
        self.fields['dob'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['mobile1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter First Mobile Number'})
        self.fields['mobile2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Second Mobile Number'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Address'})
        self.fields['roll'].widget.attrs.update({'class': 'form-control'})
        self.fields['doj'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Email'})

    class Meta:
        model = UserProfile
        fields = ('cnic', 'dob', 'gender', 'mobile1', 'mobile2', 'address', 'roll', 'doj')

