# Generated by Django 5.0.6 on 2024-06-23 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_hospitalname_register_hospitalname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='Hospitalname',
            new_name='hospitalname',
        ),
    ]
