# Generated by Django 3.1.1 on 2020-10-25 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginSystem', '0009_auto_20201023_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar_master',
            name='date',
            field=models.DateField(),
            preserve_default=False,
        ),
    ]