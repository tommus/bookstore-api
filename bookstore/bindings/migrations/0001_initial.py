# Generated by Django 3.1.2 on 2020-10-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Binding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
