# Generated by Django 3.2 on 2021-04-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamapp', '0008_auto_20210412_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='know',
            name='image',
        ),
        migrations.AddField(
            model_name='empolys',
            name='image',
            field=models.ImageField(default='', upload_to='static/stor'),
        ),
    ]
