# Generated by Django 4.2.6 on 2023-11-18 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_listings_kategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='kategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_category', to='auctions.category'),
        ),
    ]
