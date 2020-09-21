from django.contrib import admin

from .models import Product, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'seller')
    search_fields = ('title', 'description')
    raw_id_fields = ('seller',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating', 'author')
    search_fields = ('text',)
    raw_id_fields = ('author', 'product')

