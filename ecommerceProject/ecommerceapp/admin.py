from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'stock',
                    'available', 'created', 'price', 'image']
    prepopulated_fields = {'slug': ('name', )}
    list_editable = ['price', 'available', 'stock', 'image']
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
