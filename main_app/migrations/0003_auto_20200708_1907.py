# Generated by Django 3.0.6 on 2020-07-08 23:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200708_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='name',
        ),
        migrations.AddField(
            model_name='routine',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.RemoveField(
            model_name='routine',
            name='activity',
        ),
        migrations.AddField(
            model_name='routine',
            name='activity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Activity'),
            preserve_default=False,
        ),
    ]