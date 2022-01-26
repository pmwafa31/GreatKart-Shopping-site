from django.contrib import admin
from orders.models import Payment, Order, OrderProduct, ShippingAddress


# Register your models
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['order', 'created_at', 'ordered']

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]
    #readonly_fields = [field.name for field in Order._meta.fields]

class ShipAdmin(admin.ModelAdmin):
    list_display = ['user', 'order', 'full_name', 'phone', 'email', 'city']

class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in Payment._meta.fields]


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ShippingAddress, ShipAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)