# Generated by Django 4.0.7 on 2023-04-26 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completed',
            new_name='iscompleted',
        ),
    ]
