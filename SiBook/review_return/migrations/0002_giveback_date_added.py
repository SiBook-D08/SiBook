# Generated by Django 4.2.6 on 2023-10-28 11:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('review_return', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='giveback',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
