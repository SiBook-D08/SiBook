# Generated by Django 4.2.6 on 2023-10-28 12:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('review_return', '0002_giveback_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='giveback',
            name='review_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]