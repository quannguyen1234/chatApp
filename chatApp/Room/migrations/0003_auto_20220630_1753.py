# Generated by Django 3.2 on 2022-06-30 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Room', '0002_messenger'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryChatApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='messenger',
            name='member',
        ),
        migrations.DeleteModel(
            name='member_room',
        ),
        migrations.DeleteModel(
            name='Messenger',
        ),
        migrations.AddField(
            model_name='historychatapp',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.message'),
        ),
        migrations.AddField(
            model_name='historychatapp',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.room'),
        ),
        migrations.AddField(
            model_name='historychatapp',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
