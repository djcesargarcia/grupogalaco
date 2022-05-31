# Generated by Django 4.0.4 on 2022-05-31 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loadlorry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadlorry',
            name='cuantity',
            field=models.DecimalField(decimal_places=4, max_digits=5, verbose_name='Cuantity'),
        ),
        migrations.AlterField(
            model_name='loadlorry',
            name='empty_weight',
            field=models.DecimalField(decimal_places=4, max_digits=5, verbose_name='Empty Weight'),
        ),
        migrations.AlterField(
            model_name='loadlorry',
            name='mma',
            field=models.DecimalField(decimal_places=4, max_digits=5, verbose_name='MMA'),
        ),
        migrations.AlterField(
            model_name='loadlorry',
            name='tare',
            field=models.DecimalField(decimal_places=4, max_digits=5, verbose_name='Tare'),
        ),
        migrations.AlterField(
            model_name='loadlorry',
            name='total_weight',
            field=models.DecimalField(decimal_places=4, max_digits=5, verbose_name='Total Weight'),
        ),
        migrations.AlterField(
            model_name='loadlorry',
            name='volume',
            field=models.DecimalField(decimal_places=4, max_digits=5, verbose_name='Volume'),
        ),
        migrations.AlterField(
            model_name='loadlorry',
            name='weight',
            field=models.DecimalField(decimal_places=4, max_digits=5, verbose_name='Weight'),
        ),
    ]
