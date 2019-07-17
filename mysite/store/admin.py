from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Brand
from .models import Product

class MyAdminSite(AdminSite):
    site_header = 'Store administration'
    site_title = 'Store site'
    index_title = 'Administration'

admin_site = MyAdminSite(name='myadmin')

class ProductInline(admin.StackedInline):
    model = Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'brand', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['product_name']
    
    fieldsests = [
        (None, {'fields': ['product_name', 'description']}),
        ('More information', {'fields': ['pub_date', 'brand'], 'classes':
            ['collapse']})
    ]

class BrandAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)

admin_site.register(Brand, BrandAdmin)
admin_site.register(Product, ProductAdmin)

