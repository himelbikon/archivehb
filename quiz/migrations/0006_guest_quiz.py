# Generated by Django 3.1.2 on 2020-12-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20201227_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest_Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('chapter_no', models.CharField(blank=True, max_length=2)),
                ('question', models.CharField(max_length=400)),
                ('a', models.CharField(max_length=200)),
                ('b', models.CharField(max_length=200)),
                ('c', models.CharField(max_length=200)),
                ('d', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
                ('explanation', models.TextField(blank=True)),
            ],
        ),
    ]
