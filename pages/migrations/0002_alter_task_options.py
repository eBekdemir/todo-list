# Generated by Django 5.1.2 on 2024-10-22 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': [models.F('complete'), models.OrderBy(models.F('dead_line'), nulls_last=True)], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
    ]
