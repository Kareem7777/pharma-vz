# Generated by Django 3.2 on 2021-09-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prods', '0004_lux'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='p_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
