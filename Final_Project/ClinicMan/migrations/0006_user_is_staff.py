# Generated by Django 4.1 on 2022-12-01 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicMan', '0005_remove_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
