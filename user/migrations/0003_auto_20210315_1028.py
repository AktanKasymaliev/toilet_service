# Generated by Django 3.1.7 on 2021-03-15 10:28

from django.db import migrations
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_is_superuser'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.models.MyUserManager()),
            ],
        ),
    ]
