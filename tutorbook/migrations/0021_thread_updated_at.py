# Generated by Django 4.1.2 on 2022-10-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorbook', '0020_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]