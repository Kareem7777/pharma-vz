# Generated by Django 3.2 on 2021-09-07 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prods', '0006_alter_products_p_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='p_img',
            field=models.FileField(default='', upload_to='prods/static/images'),
        ),
    ]