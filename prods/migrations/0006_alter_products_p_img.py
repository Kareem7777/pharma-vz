# Generated by Django 3.2 on 2021-09-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prods', '0005_products_p_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='p_img',
            field=models.FileField(upload_to='prods/static/images'),
        ),
    ]
