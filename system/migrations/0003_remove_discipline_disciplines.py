# Generated by Django 2.2.2 on 2019-06-04 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20190605_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discipline',
            name='disciplines',
        ),
    ]