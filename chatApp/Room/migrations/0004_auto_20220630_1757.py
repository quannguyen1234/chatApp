# Generated by Django 3.2 on 2022-06-30 10:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0003_auto_20220630_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='created',
        ),
        migrations.AddField(
            model_name='historychatapp',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
