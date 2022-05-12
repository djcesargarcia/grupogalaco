# Generated by Django 4.0.4 on 2022-05-12 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_changed_my_article'),
        ('order', '0002_alter_order_code_buy_alter_order_cuantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='article.article'),
            preserve_default=False,
        ),
    ]
