from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import RentalContract, Customer, RentalItem, ItemCategory, GeneralSetting


class RentalItemAdmin(admin.ModelAdmin):
    fieldsets = [('General info', {'fields': ['name', 'category', 'description', 'notes']}),
                 ('Pricing info', {'fields': ['price', 'currency', 'minimal_rental_period_days']})]
    list_display = ['name', 'category', 'description', 'rental_price_per_day']
    list_filter = ['category']
    search_fields = ['name', 'description', 'notes']
    search_help_text = 'Start typing...'
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 7, 'cols': 60})}
    }


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [('General info', {'fields': ['customer_type', 'name', 'surname', 'company', 'address', 'note']}),
                 ('Contact info', {'fields': ['email_address', 'phone']})]
    list_display = ['company', 'name', 'surname', 'email_address', 'phone']
    search_fields = ['company', 'name', 'surname', 'note', 'email_address']


class RentalContractAdmin(admin.ModelAdmin):
    fieldsets = [('General contract details', {'fields': ['customer', 'rental_items', 'start_datetime', 'end_datetime']}),
                 ('Pricing and activity details', {'fields': ['price_without_discount',
                                                              'discount', 'paid_amount', 'total_price']})]


admin.site.register(RentalItem, RentalItemAdmin)
admin.site.register(ItemCategory)
admin.site.register(RentalContract, RentalContractAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(GeneralSetting)


# Register your models here.

