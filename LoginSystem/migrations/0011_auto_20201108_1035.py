# Generated by Django 3.1.1 on 2020-11-08 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginSystem', '0010_calendar_master_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendar_user',
            old_name='password',
            new_name='password1',
        ),
        migrations.RenameField(
            model_name='calendar_user',
            old_name='user',
            new_name='username',
        ),
        migrations.AddField(
            model_name='calendar_user',
            name='password2',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='due_date_1',
            field=models.CharField(default='-', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='due_date_1_remarks',
            field=models.CharField(default='-', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='due_date_2',
            field=models.CharField(default='-', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='due_date_2_remarks',
            field=models.CharField(default='-', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='due_date_3',
            field=models.CharField(default='-', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='due_date_3_remarks',
            field=models.CharField(default='-', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='due_date_4',
            field=models.CharField(default='-', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='due_date_4_remarks',
            field=models.CharField(default='-', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='due_date_5',
            field=models.CharField(default='-', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='due_date_5_remarks',
            field=models.CharField(default='-', max_length=100, null=True),
        ),
    ]
