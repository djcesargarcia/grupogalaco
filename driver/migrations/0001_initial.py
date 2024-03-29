# Generated by Django 4.0.4 on 2022-05-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('nif', models.CharField(max_length=9, verbose_name='NIF')),
                ('image', models.ImageField(null=True, upload_to='images/', verbose_name='Imagen')),
                ('adress', models.CharField(max_length=100, verbose_name='Adress')),
            ],
        ),
    ]
