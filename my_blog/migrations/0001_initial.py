# Generated by Django 4.2.3 on 2023-07-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=402)),
                ('email', models.CharField(max_length=402)),
                ('phone', models.CharField(max_length=402)),
            ],
        ),
    ]
