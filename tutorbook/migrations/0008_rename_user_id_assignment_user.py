# Generated by Django 4.1.2 on 2022-10-16 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorbook', '0007_rename_level_tutor_levels_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='user_id',
            new_name='user',
        ),
    ]
