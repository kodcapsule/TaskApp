# Generated by Django 4.2.6 on 2023-11-11 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_task_status_alter_task_taskcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskCategory',
            field=models.CharField(choices=[('FE', 'FrontEnd'), ('BE', 'Backend'), ('DV', 'DevOps'), ('UI/UX', 'UI/UX')], default='Frontend', max_length=600),
        ),
    ]
