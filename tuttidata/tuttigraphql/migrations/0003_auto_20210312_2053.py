# Generated by Django 3.1.7 on 2021-03-12 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tuttigraphql', '0002_auto_20210312_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='ad',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tuttigraphql.user'),
        ),
    ]
