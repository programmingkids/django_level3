# Generated by Django 3.1 on 2021-06-04 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_character_weapon'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(default=0)),
                ('hobby', models.CharField(max_length=50)),
            ],
        ),
    ]
