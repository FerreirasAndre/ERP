# Generated by Django 5.2.1 on 2025-06-07 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='description',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='preco',
            new_name='price',
        ),
    ]
