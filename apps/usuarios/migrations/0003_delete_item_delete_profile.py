# Generated by Django 5.1.1 on 2024-10-11 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_item_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
