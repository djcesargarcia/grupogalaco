# Generated by Django 4.0.4 on 2022-04-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code_buy',
            field=models.IntegerField(verbose_name='Code Buy'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cuantity',
            field=models.IntegerField(verbose_name='Cuantity'),
        ),
    ]
