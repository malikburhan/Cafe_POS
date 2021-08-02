from django import forms
from .models import Customer


# Register your forms here.
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "mobile", "address"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Name', 'autofocus':True})
        self.fields['mobile'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Mobile Number'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Address'})
