# Generated by Django 4.2.4 on 2023-09-18 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0005_rename_created_at_trainer_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainer',
            old_name='date',
            new_name='created_at',
        ),
    ]
