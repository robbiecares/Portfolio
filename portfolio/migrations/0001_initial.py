# Generated by Django 3.1.7 on 2021-03-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True)),
                ('status', models.CharField(choices=[('s', 'started'), ('a', 'active'), ('c', 'completed')], default='s', max_length=1)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
