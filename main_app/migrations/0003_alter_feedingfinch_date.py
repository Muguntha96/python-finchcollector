# Generated by Django 4.2.6 on 2023-11-01 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feedingfinch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedingfinch',
            name='date',
            field=models.DateField(verbose_name='Feeding Date'),
        ),
    ]
