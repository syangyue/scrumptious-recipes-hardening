from django.contrib import admin

from .models import MealPlan


class MealPlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(MealPlan, MealPlanAdmin)
