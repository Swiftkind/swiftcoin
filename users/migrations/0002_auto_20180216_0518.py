# Generated by Django 2.0.2 on 2018-02-16 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
