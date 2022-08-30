# Generated by Django 3.2 on 2022-08-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(error_messages={'unique': 'A user with that email address already exists.'}, max_length=256, unique=True, verbose_name='email'),
        ),
    ]