# Generated by Django 2.1.2 on 2018-10-26 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0008_auto_20181026_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2018, 10, 26, 8, 48, 4, 435776)),
        ),
    ]
