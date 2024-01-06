# Generated by Django 4.2.7 on 2024-01-05 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fooditems', '0004_foodlog'),
        ('caloriesTracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyFoodTake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooditems.fooditems')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
