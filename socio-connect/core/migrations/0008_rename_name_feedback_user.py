# Generated by Django 4.1.6 on 2023-03-27 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='name',
            new_name='user',
        ),
    ]