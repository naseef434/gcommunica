# Generated by Django 3.1.2 on 2020-10-24 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panchayath', models.CharField(max_length=30)),
                ('ward', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]