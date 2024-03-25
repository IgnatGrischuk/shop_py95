from django.contrib import admin
from .models import (Category, Product, Discount, Seller, Order,
                     CashBack, Promocode, ProductImage)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('article', 'name', 'price')
    search_fields = ('article', 'name', 'category__name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Seller)
admin.site.register(CashBack)
admin.site.register(Order)
admin.site.register(ProductImage)
admin.site.register(Promocode)