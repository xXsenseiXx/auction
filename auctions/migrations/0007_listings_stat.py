# Generated by Django 4.2.6 on 2023-11-16 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_remove_listings_category_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='stat',
            field=models.CharField(choices=[('active', 'Active'), ('closed', 'Closed')], default='active', max_length=10),
        ),
    ]