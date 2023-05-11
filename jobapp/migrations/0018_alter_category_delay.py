# Generated by Django 4.1.4 on 2023-05-11 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0017_category_delay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='delay',
            field=models.DecimalField(blank=True, choices=[('0.1', '0.1'), ('0.3', '0.3'), ('0.5', '0.5'), ('0.7', '0.7')], decimal_places=1, max_digits=2, null=True),
        ),
    ]
