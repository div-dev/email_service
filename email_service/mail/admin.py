from django.contrib import admin
from .models import emailRecord

@admin.register(emailRecord)
class EmailRecordAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'next_interval', 'last_send_at')
