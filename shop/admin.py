from django.contrib import admin
from .models import *
# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']

admin.site.register(categ,catadmin)

class prodadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','img','desc','stock','price','category','available']
    list_editable=['stock','price','img','available']

admin.site.register(products,prodadmin)