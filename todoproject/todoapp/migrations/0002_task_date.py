# Generated by Django 4.1.5 on 2023-03-15 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2022-02-02'),
            preserve_default=False,
        ),
    ]
