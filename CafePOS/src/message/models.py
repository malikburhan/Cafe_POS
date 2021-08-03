from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class OutBox(models.Model):
    mobile = models.CharField(max_length=11)
    message = models.TextField()
    status = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='OutBox.creator+', null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='OutBox.updater+', null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='OutBox.deleter+', null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.mobile

    def __str__(self):
        return self.mobile

    class Meta:
        ordering = ['id']
        verbose_name = "OutBox"
        verbose_name_plural = "OutBox"


class MobileMac(models.Model):
    mac = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='MobileMac.creator+', null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='MobileMac.updater+', null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='MobileMac.deleter+', null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.mac

    def __str__(self):
        return self.mac

    class Meta:
        ordering = ['id']
        verbose_name = "MobileMac"
        verbose_name_plural = "MobileMac"
