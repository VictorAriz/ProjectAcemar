from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User
# from apps.report.models import Report

# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


# class Levels(models.Model):
#     name = models.CharField(max_length=30, blank=True)
#     def __str__(self): return self.name



# class ReportType(models.Model):
#     name = models.CharField(max_length=50, null=True)

#     def __str__(self):
#         texto = "{0}"
#         return texto.format(self.name)

# class Categories(models.Model):
#     name = models.CharField(max_length=50, null=True)

#     def __str__(self):
#         texto = "{0}"
#         return texto.format(self.name)


# class Report(models.Model):
#     name = models.CharField(max_length=50, null=True)
#     biData = models.CharField(max_length=50, null=True)
#     sqlData = models.CharField(max_length=50, null=True)
#     description = models.TextField(null=True)
#     text = models.CharField(max_length=50, null=True)
#     fileType = models.ForeignKey(ReportType, on_delete=models.SET_NULL, null=True)
#     levels = models.ManyToManyField(Levels)
#     fileReport = models.FileField(upload_to="reportFiles", null=True)
#     imageReport = models.ImageField(upload_to="reportImage",null=True)
#     viewsReport = models.IntegerField(null=True)
#     uses = models.IntegerField(null=True)
#     categories = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)


#     def __str__(self):
#         texto = "{0}"
#         return texto.format(self.name)




class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, blank=True)
    nationalId = models.CharField(max_length=30, null=True, blank=True)
    deviceId = models.CharField(max_length=500, blank=True)
    # levels = models.ForeignKey(Levels, on_delete=models.SET_NULL, null=True)
    # singleLevels = models.ManyToManyField(Report)