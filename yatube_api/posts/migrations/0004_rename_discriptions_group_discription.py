# Generated by Django 3.2.16 on 2023-01-16 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_follower_follow_following'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='discriptions',
            new_name='discription',
        ),
    ]
