from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Shelter(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True, verbose_name="Адресс")
    email = models.CharField(max_length=100, null=True, verbose_name="Почта")
    phone = models.CharField(max_length=100, null=True, verbose_name="Телефон")

    def __str__(self):
        return self.address
