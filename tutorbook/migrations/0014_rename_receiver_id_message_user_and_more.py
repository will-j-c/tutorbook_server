# Generated by Django 4.1.2 on 2022-10-16 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorbook', '0013_rename_user_two_thread_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='receiver_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender_id',
        ),
        migrations.AddField(
            model_name='message',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sender_id', to='tutorbook.tutor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='tutor_is_sender',
            field=models.BooleanField(default=False),
        ),
    ]
