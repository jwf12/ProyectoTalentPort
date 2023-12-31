# Generated by Django 4.2.7 on 2023-11-22 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendlist_set', to=settings.AUTH_USER_MODEL)),
                ('userlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userlist_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
