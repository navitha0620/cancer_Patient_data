# Generated by Django 5.0.6 on 2024-06-22 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_fullname_register_branchaddress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='subject',
            field=models.CharField(default='Nothing', max_length=150),
            preserve_default=False,
        ),
    ]