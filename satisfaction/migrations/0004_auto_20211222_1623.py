# Generated by Django 3.0.5 on 2021-12-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satisfaction', '0003_auto_20211221_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satisfaction',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
