# Generated by Django 2.2.12 on 2020-04-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0006_remove_ds_year_of_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ds',
            name='initial',
            field=models.CharField(max_length=10, verbose_name='initial of student'),
        ),
    ]
