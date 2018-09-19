from django.contrib import admin
from itempage.models import Item, Order, OrderItem


class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_code', 'item_name', 'price')


# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
