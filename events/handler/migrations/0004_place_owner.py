# Generated by Django 3.0 on 2020-01-23 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('handler', '0003_user_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='handler.User'),
        ),
    ]
