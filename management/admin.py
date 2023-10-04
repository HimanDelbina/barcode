from django.contrib import admin

from .models import *
# Register your models here.


class BarCodeAdmin(admin.ModelAdmin):
    fields = ['title', 'isbn','barcode']
    list_display = ['title', 'isbn', 'image_tag']
    
    
admin.site.register(BarCodeModel,BarCodeAdmin)