# Generated by Django 4.2.7 on 2024-01-05 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fooditems', '0004_foodlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListFoodItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=100)),
                ('calories', models.PositiveIntegerField()),
                ('List', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fooditems.fooditems')),
            ],
        ),
    ]
