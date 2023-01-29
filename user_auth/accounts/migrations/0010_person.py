# Generated by Django 4.1.4 on 2022-12-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_profile_address_alter_profile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('birth_date', models.DateField()),
                ('location', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
