# Generated by Django 3.2.9 on 2021-11-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='profiles'),
        ),
    ]
