# Generated by Django 2.2 on 2021-05-02 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cortinas', '0002_auto_20210417_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
    ]
