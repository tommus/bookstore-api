# Generated by Django 2.1.2 on 2018-10-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20181022_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binding',
            name='description',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
