# Generated by Django 3.0.4 on 2020-03-11 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='question',
            new_name='article',
        ),
    ]