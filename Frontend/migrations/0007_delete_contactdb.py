# Generated by Django 4.2.6 on 2023-12-17 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0006_remove_contactdb_mobile_remove_contactdb_uname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contactDB',
        ),
    ]
