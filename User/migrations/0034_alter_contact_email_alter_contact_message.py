# Generated by Django 5.1.6 on 2025-04-03 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0033_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
    ]
