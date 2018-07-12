from django.contrib import admin
from .models import Room, Ticket

# admin.site.register(Room)
# admin.site.register(Ticket)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'no_new_tickets')
    list_filter = ('status', 'no_new_tickets')


admin.site.register(Room, RoomAdmin)


class TicketAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ticket, TicketAdmin)

admin.site.site_header = "HWH Room Statuses"
admin.site.site_title = "HWH Room Statuses"
admin.site.index_title = "Dashboard"
