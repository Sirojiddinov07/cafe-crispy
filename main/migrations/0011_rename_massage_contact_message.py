# Generated by Django 4.1.3 on 2022-12-01 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_contact_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='massage',
            new_name='message',
        ),
    ]
