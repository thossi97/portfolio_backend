# Generated by Django 3.1.2 on 2020-11-21 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201121_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='git',
            field=models.URLField(blank=True),
        ),
    ]
