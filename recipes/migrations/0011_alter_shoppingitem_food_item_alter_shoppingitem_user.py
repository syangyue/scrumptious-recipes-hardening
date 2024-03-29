# Generated by Django 4.0.3 on 2022-09-22 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0010_shoppingitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingitem',
            name='food_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shoppingitems', to='recipes.fooditem'),
        ),
        migrations.AlterField(
            model_name='shoppingitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoppingitems', to=settings.AUTH_USER_MODEL),
        ),
    ]
