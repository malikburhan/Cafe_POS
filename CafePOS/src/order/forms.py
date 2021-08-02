from django import forms
from menu.models import Category, Menu, Size


# Register your forms here.
class OrderForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(is_deleted=False))
    menu = forms.ModelChoiceField(queryset=Menu.objects.none())
    size = forms.ModelChoiceField(queryset=Size.objects.none())
    quantity = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['menu'].widget.attrs.update({'class': 'form-control'})
        self.fields['size'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control', 'value':'1', 'min': '1'})
