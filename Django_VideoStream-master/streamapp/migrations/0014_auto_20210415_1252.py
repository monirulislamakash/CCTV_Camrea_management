# Generated by Django 3.2 on 2021-04-15 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streamapp', '0013_auto_20210415_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cam_configer2',
            old_name='camera_number',
            new_name='camera_number2',
        ),
        migrations.RenameField(
            model_name='cam_configer2',
            old_name='ip_address',
            new_name='ip_address2',
        ),
        migrations.RenameField(
            model_name='cam_configer2',
            old_name='name',
            new_name='name2',
        ),
        migrations.RenameField(
            model_name='cam_configer2',
            old_name='pasw',
            new_name='pasw2',
        ),
    ]