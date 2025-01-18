# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Foot Traffic(models.Model):

    #__Foot Traffic_FIELDS__
    datetime = models.DateTimeField(blank=True, null=True, default=timezone.now)
    foot traffic = models.IntegerField(null=True, blank=True)

    #__Foot Traffic_FIELDS__END

    class Meta:
        verbose_name        = _("Foot Traffic")
        verbose_name_plural = _("Foot Traffic")



#__MODELS__END
