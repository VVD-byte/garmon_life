from django.contrib import admin
from .models import Special, Work, Category, Paper, Questions


class AdminPaper(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Special)
admin.site.register(Work)
admin.site.register(Category)
admin.site.register(Paper, AdminPaper)
admin.site.register(Questions)
