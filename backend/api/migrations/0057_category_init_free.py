# Generated by Django 2.0.7 on 2018-07-26 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_auto_20180725_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='init_free',
            field=models.IntegerField(default=0),
        ),
    ]
