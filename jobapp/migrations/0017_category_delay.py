# Generated by Django 4.1.4 on 2023-05-11 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0016_alter_applicant_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='delay',
            field=models.IntegerField(blank=True, choices=[('0.1', '0.1'), ('0.3', '0.3'), ('0.5', '0.5'), ('0.7', '0.7')], null=True),
        ),
    ]
