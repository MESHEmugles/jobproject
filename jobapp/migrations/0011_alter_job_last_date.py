# Generated by Django 4.1.4 on 2023-05-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0010_alter_job_last_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='last_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
