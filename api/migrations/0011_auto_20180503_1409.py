# Generated by Django 2.0.4 on 2018-05-03 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20180503_1336'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='imageprofile',
            unique_together={('image', 'profile')},
        ),
    ]
