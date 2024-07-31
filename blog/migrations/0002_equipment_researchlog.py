# Generated by Django 5.0.6 on 2024-06-17 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('date_acquired', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ResearchLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiment_name', models.CharField(max_length=200)),
                ('researcher', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('notes', models.TextField()),
            ],
        ),
    ]