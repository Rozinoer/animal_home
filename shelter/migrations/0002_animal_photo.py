# Generated by Django 3.1.2 on 2020-12-22 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='photo',
            field=models.ImageField(blank=True, upload_to='animal/%Y/%m/%d'),
        ),
    ]
