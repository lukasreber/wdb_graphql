# Generated by Django 3.1.7 on 2021-03-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuttigraphql', '0005_ad_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(blank=True, default=None),
        ),
    ]
