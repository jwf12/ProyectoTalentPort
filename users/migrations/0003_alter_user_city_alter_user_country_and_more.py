# Generated by Django 4.2.7 on 2023-11-08 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_city_alter_user_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='lenguages1',
            field=models.CharField(blank=True, choices=[('1', 'Js'), ('2', 'Python'), ('3', 'Java'), ('4', 'Rust'), ('5', 'Go')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='lenguages2',
            field=models.CharField(blank=True, choices=[('1', 'Js'), ('2', 'Python'), ('3', 'Java'), ('4', 'Rust'), ('5', 'Go')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='open_work',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='stack',
            field=models.CharField(blank=True, choices=[('1', 'Front-End'), ('2', 'Back-End'), ('3', 'Full-Stack')], max_length=20, null=True),
        ),
    ]