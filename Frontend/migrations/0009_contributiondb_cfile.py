# Generated by Django 4.2.6 on 2023-12-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0008_delete_campdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributiondb',
            name='Cfile',
            field=models.FileField(blank=True, null=True, upload_to='DFILE'),
        ),
    ]
