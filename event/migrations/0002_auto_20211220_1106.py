# Generated by Django 3.0.5 on 2021-12-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='classification',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
