# Generated by Django 3.1.2 on 2020-12-03 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HSC_Biology_1st',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_no', models.CharField(max_length=2)),
                ('chapter_name', models.CharField(max_length=50)),
                ('caption', models.CharField(max_length=150)),
                ('content', models.TextField()),
            ],
        ),
    ]
