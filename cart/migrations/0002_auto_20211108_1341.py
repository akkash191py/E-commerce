# Generated by Django 3.2.8 on 2021-11-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name_plural': 'Cart'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name_plural': 'Cart Items'},
        ),
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
