from django.contrib import admin
from .models import Profile, Shelter


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Shelter)