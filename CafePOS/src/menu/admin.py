from django.contrib import admin
from .models import Category, Size, Menu, Price

# Register your models here.

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Menu)
admin.site.register(Price)