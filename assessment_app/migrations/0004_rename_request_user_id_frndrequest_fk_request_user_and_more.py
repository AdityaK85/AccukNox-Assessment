# Generated by Django 5.0.6 on 2024-05-31 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_app', '0003_frndrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frndrequest',
            old_name='request_user_id',
            new_name='fk_request_user',
        ),
        migrations.RenameField(
            model_name='frndrequest',
            old_name='user_id',
            new_name='fk_user',
        ),
    ]