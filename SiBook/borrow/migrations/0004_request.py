# Generated by Django 4.2.6 on 2023-10-25 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0003_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
            ],
        ),
    ]