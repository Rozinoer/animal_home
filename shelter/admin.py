from django.contrib import admin

from .models import Animal, Color, Weight

admin.site.register(Animal)
admin.site.register(Color)
admin.site.register(Weight)
