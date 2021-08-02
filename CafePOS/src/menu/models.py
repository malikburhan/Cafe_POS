from django.contrib.auth.models import User
from django.db import models
import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    """  developer """
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Category.creator+', null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Category.updater+', null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Category.deleter+', null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    """  developer """

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['id']
        verbose_name = "1. Category"
        verbose_name_plural = "1. Category"


class Size(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sizecategory')
    size = models.CharField(max_length=100)

    """  developer """
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Size.creator+', null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Size.updater+', null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Size.deleter+', null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    """  developer """

    def __unicode__(self):
        return f'{self.category.name} - {self.size}'

    def __str__(self):
        return f'{self.category.name} - {self.size}'

    class Meta:
        ordering = ['id']
        verbose_name = "2. Size"
        verbose_name_plural = "2. Size"


class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menucategory')
    name = models.CharField(max_length=100)

    """  developer """
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Menu.creator+', null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Menu.updater+', null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Menu.deleter+', null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    """  developer """

    def __unicode__(self):
        return f'{self.category.name} - {self.name}'

    def __str__(self):
        return f'{self.category.name} - {self.name}'

    class Meta:
        ordering = ['id']
        verbose_name = "3. Menu"
        verbose_name_plural = "3. Menu"


class Price(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='pricemenu')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='pricesize')
    price = models.IntegerField(default=0)

    """  developer """
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Price.creator+', null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Price.updater+', null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Price.deleter+', null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    """  developer """

    def __unicode__(self):
        return f'{self.price}'

    def __str__(self):
        return f'{self.price}'

    class Meta:
        ordering = ['id']
        verbose_name = "4. Price"
        verbose_name_plural = "4. Price"