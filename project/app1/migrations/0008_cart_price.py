# Generated by Django 5.1.1 on 2024-09-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_delete_cart_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
