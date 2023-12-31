# Generated by Django 4.2.5 on 2023-11-01 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country_code',
            field=models.CharField(blank=True, default=None, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fav_mov',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
    ]
