# Generated by Django 3.1.7 on 2021-03-17 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuttigraphql', '0008_auto_20210317_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]
