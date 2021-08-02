from django import forms
from .models import Category, Menu


# Register your forms here.
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Name', 'autofocus':True})


class MenuForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(is_deleted=False))

    class Meta:
        model = Menu
        fields = ["category", "name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Name', 'autofocus':True})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})