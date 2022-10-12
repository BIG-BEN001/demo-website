from django.contrib import admin
from .models import EmailMessage

# Register your models here.

@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject',)