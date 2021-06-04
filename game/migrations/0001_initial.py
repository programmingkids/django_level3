# Generated by Django 3.1 on 2021-06-02 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hp', models.IntegerField(default=0)),
                ('mp', models.IntegerField(default=0)),
                ('type', models.IntegerField(choices=[(1, '炎属性'), (2, '水属性'), (3, '闇属性')])),
            ],
        ),
    ]