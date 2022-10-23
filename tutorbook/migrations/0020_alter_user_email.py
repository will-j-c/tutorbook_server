# Generated by Django 4.1.2 on 2022-10-23 10:59

from django.db import migrations
import tutorbook.models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorbook', '0019_rename_thread_id_message_thread_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=tutorbook.models.LowercaseEmailField(max_length=254, unique=True),
        ),
    ]
