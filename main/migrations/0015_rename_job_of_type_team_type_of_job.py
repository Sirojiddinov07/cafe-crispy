# Generated by Django 4.1.3 on 2022-12-07 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_delete_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='job_of_type',
            new_name='type_of_job',
        ),
    ]
