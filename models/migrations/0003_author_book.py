# Generated by Django 4.2.3 on 2023-08-12 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=300)),
                ('authors', models.ManyToManyField(to='models.author')),
            ],
        ),
    ]
