# Generated by Django 4.1.7 on 2023-04-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number_of_guests', models.IntegerField()),
                ('booking_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Booking Records',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menu Items',
            },
        ),
    ]
