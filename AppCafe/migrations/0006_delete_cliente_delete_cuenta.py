# Generated by Django 5.0.6 on 2024-06-22 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCafe', '0005_delete_mesero'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Cuenta',
        ),
    ]