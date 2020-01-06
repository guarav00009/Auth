from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.db.models import Value
from django.db.models.functions import Concat
from ckeditor_uploader.fields import RichTextUploadingField
import os


# Create your models here.
# class Users(models.Model):
#     employee_id = models.CharField(max_length=10,unique=True)
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()
#     ranking = models.FloatField()

#     def upload_photo(self,filename):
#         path = "hrm/photo/{}".format(filename)
#         return path

#     photo = models.ImageField(upload_to=upload_photo,null=True,blank=True)

#     def upload_file(self,filename):
#         path = "hrm/file/{}".format(filename)
#         return path

#     resume = models.ImageField(upload_to=upload_file,null=True,blank=True)

#     def __str__(self):
#         return f"{self.employee_id} - {self.name}"

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(_('role'), max_length=255, blank=True)
    is_email_verified = models.BooleanField(
        _('is email verified'), default=False)
    password_change_date = models.DateField(
        _('password change date'), blank=True, null=True)
    image = models.ImageField(
        upload_to='profile/', default='profile/user.png', blank=True, null=True)
    STATUS_CHOICES = (
        (1, 'Active'),
        (0, 'Inactive'),
        (2, 'Deleted'),
    )
    is_active = models.IntegerField(
        _('status'), choices=STATUS_CHOICES, default=1)

    is_staff = models.BooleanField(
        _('is admin'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    COUNTRY_CHOICE = [
        ('IN', 'India'),
        ('US', 'USA'),
        ('UK', 'UK'),
        #('SENIOR', 'Senior'),
    ]
    country = models.CharField(
        max_length=2,
        choices=COUNTRY_CHOICE,
        default='US',
    )
    deleted_at = models.DateField(_('deteted at'), blank=True, null=True)
    deleted_by_id = models.IntegerField(_('deteted by'), blank=True, null=True)

    def __str__(self):
        return self.username

    def get_name(self):
        return self.first_name.capitalize() + ' ' + self.last_name.capitalize()

    class Meta:
        verbose_name_plural = 'Users'

    get_name.allow_tags = True
    get_name.short_description = 'name'
    get_name.admin_order_field = Concat('first_name', Value(' '), 'last_name')