# Generated by Django 4.0.2 on 2022-04-13 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sneaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=101)),
                ('description', models.TextField(max_length=250)),
                ('release', models.DateField(verbose_name='Release Date')),
            ],
        ),
    ]
