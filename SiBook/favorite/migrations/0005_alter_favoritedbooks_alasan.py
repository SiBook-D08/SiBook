# Generated by Django 4.2.6 on 2023-10-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite', '0004_alter_favoritedbooks_alasan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritedbooks',
            name='alasan',
            field=models.CharField(default='', max_length=255),
        ),
    ]
