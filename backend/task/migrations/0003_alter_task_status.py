# Generated by Django 4.2.6 on 2023-11-11 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_userprofile_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('incomplete', 'complete'), ('complete', 'Complete')], default='Incomplete', max_length=100),
        ),
    ]
