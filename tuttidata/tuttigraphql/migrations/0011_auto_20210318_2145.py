# Generated by Django 3.1.7 on 2021-03-18 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuttigraphql', '0010_auto_20210317_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='category',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='ad',
            name='dateadded',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ad',
            name='nr',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='price',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='views',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='zip',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
