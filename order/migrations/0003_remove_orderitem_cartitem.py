# Generated by Django 3.2.8 on 2021-11-11 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20211111_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='cartitem',
        ),
    ]
