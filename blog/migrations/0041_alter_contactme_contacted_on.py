# Generated by Django 4.0.2 on 2022-07-18 07:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_alter_contactme_contacted_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactme',
            name='Contacted_On',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
