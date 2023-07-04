# Generated by Django 4.1 on 2022-08-25 03:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('category', models.CharField(choices=[('FASH', 'Fashion'), ('ELEC', 'Electronics'), ('TOYS', 'Toys')], default='FASH', max_length=4)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('closed', models.BooleanField(default=False)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]