# Generated by Django 4.1.3 on 2022-12-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_about_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='foods',
            name='category',
            field=models.CharField(choices=[('foods', 'foods'), ('drink', 'drink'), ('salad', 'salad'), ('desert', 'desert')], default='foods', max_length=100),
        ),
    ]
