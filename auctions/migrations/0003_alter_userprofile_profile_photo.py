# Generated by Django 4.0.3 on 2022-04-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_userprofile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, default='auction_images/default/default.svg', null=True, upload_to='photos/profile'),
        ),
    ]
