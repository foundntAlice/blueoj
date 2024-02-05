from django.contrib import admin
from .models import Problem


class ProblemAdmin(admin.ModelAdmin):
    list_display = ("name", "time_limit", "public_date",)

admin.site.register(Problem, ProblemAdmin)