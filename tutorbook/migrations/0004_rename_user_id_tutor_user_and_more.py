# Generated by Django 4.1.2 on 2022-10-15 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorbook', '0003_user_profile_img_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutor',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_type_id',
            new_name='user_type',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='published_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='published_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='subscription_expires_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]