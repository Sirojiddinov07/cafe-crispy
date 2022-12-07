# Generated by Django 4.1.3 on 2022-11-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='media/')),
                ('special', models.CharField(choices=[('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner')], max_length=100)),
                ('rating', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('reviews', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
