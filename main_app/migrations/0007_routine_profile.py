# Generated by Django 3.0.6 on 2020-07-09 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='routine',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Profile'),
            preserve_default=False,
        ),
    ]
