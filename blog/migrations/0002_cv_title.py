# Generated by Django 3.1 on 2020-08-31 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='title',
            field=models.CharField(default="Oscar's CV", max_length=200),
        ),
    ]
