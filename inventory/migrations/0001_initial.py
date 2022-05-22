# Generated by Django 4.0 on 2022-05-22 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('capacity', models.IntegerField(default=500)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('amount', models.IntegerField(default=0)),
                ('unit_price', models.FloatField(default=0.0)),
                ('storage_space', models.IntegerField(default=1)),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='inventory.warehouse')),
            ],
        ),
    ]
