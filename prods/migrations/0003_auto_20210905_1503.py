# Generated by Django 3.2 on 2021-09-05 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prods', '0002_alter_products_p_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
        migrations.RemoveField(
            model_name='products',
            name='p_img',
        ),
    ]