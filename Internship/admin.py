from django.contrib import admin
from .models import category
from .models import products

class categorydisplay(admin.ModelAdmin):
    display = ('categoryname')

class productdisplay(admin.ModelAdmin):
    list_display = ('categoryname','product_name','price','quantity','description')

admin.site.register(products,productdisplay)
admin.site.register(category,categorydisplay)
# Register your models here.
