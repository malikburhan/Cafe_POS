from django.contrib import admin
from .models import MobileMac, OutBox

# Register your models here.


class MobileMacModelAdmin(admin.ModelAdmin):
    list_display = ["mac", "status", "updated", "deleted", "is_deleted"]
    list_display_links = ["mac", "status"]
    search_fields = ["mac", "status"]

    class Meta:
        model = MobileMac


class OutBoxModelAdmin(admin.ModelAdmin):
    list_display = ["mobile", "message", "status", "updated", "deleted", "is_deleted"]
    list_display_links = ["mobile"]
    search_fields = ["mobile"]

    class Meta:
        model = OutBox


admin.site.register(MobileMac, MobileMacModelAdmin)
admin.site.register(OutBox, OutBoxModelAdmin)

