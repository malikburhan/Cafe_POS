from django.contrib import admin
from .models import Customer


# Register your models here.
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'mobile', 'address'
    ]
    list_display_links = ["name"]
    search_fields = ["name"]

    class Meta:
        model = Customer


admin.site.register(Customer, CustomerModelAdmin)

