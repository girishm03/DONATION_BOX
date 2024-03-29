# Generated by Django 4.2.6 on 2023-11-04 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_persondb'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ename', models.CharField(blank=True, max_length=100, null=True)),
                ('Ebudget', models.IntegerField(blank=True, null=True)),
                ('Edays', models.CharField(blank=True, max_length=100, null=True)),
                ('Etime', models.CharField(blank=True, max_length=100, null=True)),
                ('Edescription', models.CharField(blank=True, max_length=100, null=True)),
                ('Eimage', models.ImageField(blank=True, null=True, upload_to='EIMAGE')),
            ],
        ),
    ]
