# Generated by Django 3.2.7 on 2021-10-02 07:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0010_member'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='LibraryMember',
        ),
    ]
