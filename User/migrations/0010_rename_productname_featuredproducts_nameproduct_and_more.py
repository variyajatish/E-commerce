# Generated by Django 5.1.3 on 2025-01-31 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_featuredproducts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featuredproducts',
            old_name='productname',
            new_name='nameproduct',
        ),
        migrations.RenameField(
            model_name='featuredproducts',
            old_name='newproduct',
            new_name='newimg',
        ),
    ]
