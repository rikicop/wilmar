# Generated by Django 2.2 on 2021-05-12 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cortinas', '0006_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='description',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='img',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
