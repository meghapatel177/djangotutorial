# Generated by Django 4.0.5 on 2022-07-01 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software_name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='pictures')),
            ],
        ),
    ]
