# Generated by Django 3.2.8 on 2022-01-06 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
