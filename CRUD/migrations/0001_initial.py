# Generated by Django 3.1 on 2020-08-12 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('price', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
