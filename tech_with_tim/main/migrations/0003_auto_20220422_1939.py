# Generated by Django 3.2.8 on 2022-04-22 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220422_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='contact',
        ),
    ]
