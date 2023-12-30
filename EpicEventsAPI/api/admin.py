from django.contrib import admin
from .models import Client, Contract, Event


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone',
                    'compagny_name', 'last_update',
                    'creation_date', 'support_contact')


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('total_amount', 'remaining_amount', 'status',
                    'creation_date', 'client', 'support_contact')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'contract', 'client', 'date_start',
                    'date_end', 'support_contact')
