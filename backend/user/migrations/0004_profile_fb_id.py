# Generated by Django 3.1.3 on 2021-02-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201114_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fb_id',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
