from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=11, unique=True, error_messages={'unique':"This number has already been registered."})
    address = models.CharField(max_length=120, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Customer.creator+', null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Customer.updater+', null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Customer.deleter+', null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = "Customer"
        verbose_name_plural = "Customer"