# Generated by Django 3.2 on 2022-08-30 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_data_migration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-created',), 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]
