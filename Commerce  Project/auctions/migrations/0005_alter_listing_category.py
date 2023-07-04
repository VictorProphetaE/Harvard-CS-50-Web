# Generated by Django 4.1 on 2022-09-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_watchlist_comment_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('CLOT', 'Clothes'), ('BOOK', 'Books'), ('ELEC', 'Electronics'), ('TOYS', 'Toys')], default='CLOT', max_length=4),
        ),
    ]