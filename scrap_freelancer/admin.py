from django.contrib import admin
from .models import Scrap

# Register your models here.
@admin.register(Scrap)
class ScrapAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')