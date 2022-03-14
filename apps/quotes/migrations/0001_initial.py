# Generated by Django 4.0.1 on 2022-03-11 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.PositiveSmallIntegerField(null=True)),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('typematerial', models.CharField(max_length=50, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
