from django.db import models
from django.conf import settings
USER_MODEL = settings.AUTH_USER_MODEL


class MealPlan(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    owner = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE
    )
    recipes = models.ManyToManyField(
        "recipes.Recipe",
        related_name="meal_plans"
    )
