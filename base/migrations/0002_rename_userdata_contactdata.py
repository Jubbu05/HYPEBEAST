# Generated by Django 4.0.5 on 2022-06-30 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserData',
            new_name='ContactData',
        ),
    ]
