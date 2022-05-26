# Generated by Django 4.0.4 on 2022-05-26 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('postal_code', models.CharField(max_length=100, verbose_name='Postal Code')),
                ('image', models.ImageField(null=True, upload_to='images/', verbose_name='Imagen')),
                ('municipality', models.CharField(max_length=50, verbose_name='Municipality')),
            ],
        ),
    ]
