# Generated by Django 4.2.6 on 2023-11-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_alter_listings_kategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid',
            field=models.IntegerField(default=0),
        ),
    ]
