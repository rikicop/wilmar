# Generated by Django 2.2 on 2021-05-02 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cortinas', '0004_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
