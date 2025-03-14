# Generated by Django 5.1.6 on 2025-03-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=15)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=27)),
                ('miliage', models.PositiveIntegerField(blank=True, null=True)),
                ('fuel_type', models.CharField(max_length=10)),
                ('desciptions', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='car_images/')),
            ],
            options={
                'verbose_name': 'Cars',
                'ordering': ['update_at'],
            },
        ),
    ]
