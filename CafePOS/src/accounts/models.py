from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Trans', 'Trans')
    ]
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Order Taker', 'Order Taker'),
        ('Sheff', 'Sheff')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cnic = models.CharField(max_length=13, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=6, null=True, blank=True, choices=GENDER_CHOICES)
    mobile1 = models.CharField(max_length=11, null=True, blank=True)
    mobile2 = models.CharField(max_length=11, null=True, blank=True)
    roll = models.CharField(max_length=20, null=True, blank=True, choices=ROLE_CHOICES)
    address = models.CharField(max_length=120, null=True, blank=True)
    doj = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserProfile.creator+', null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserProfile.updater+', null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserProfile.deleter+', null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.first_name

    def __str__(self):
        return self.user.first_name

    class Meta:
        ordering = ['id']
        verbose_name = "User Profile"
        verbose_name_plural = "User Profile"

