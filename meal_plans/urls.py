from django.urls import path
from .views import (
    MealPlanListView,
    MealPlanDetailView,
    MealPlanCreateView,
    MealPlanUpdateView,
    MealPlanDeleteView
)


urlpatterns = [
    path("", MealPlanListView.as_view(), name="meal_plans_list"),
    path("<int:pk>/", MealPlanDetailView.as_view(), name="meal_plan_detail"),
    path("create/", MealPlanCreateView.as_view(), name="meal_plan_create"),
    path("<int:pk>/edit/", MealPlanUpdateView.as_view(), name="meal_plan_edit"),
    path("<int:pk>/delete/", MealPlanDeleteView.as_view(),
         name="meal_plan_delete")
]
