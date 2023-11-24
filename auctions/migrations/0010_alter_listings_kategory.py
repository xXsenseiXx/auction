# Generated by Django 4.2.6 on 2023-11-18 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_category_code_listings_kategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='kategory',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_category', to='auctions.category'),
        ),
    ]
