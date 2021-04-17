# Generated by Django 3.1.7 on 2021-04-17 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('a', 'active'), ('i', 'inactive'), ('c', 'completed')], default='i', max_length=1)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('url', models.URLField(blank=True)),
                ('repository', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio.activity')),
            ],
            bases=('portfolio.activity',),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio.activity')),
                ('type', models.CharField(choices=[('b', 'book'), ('e', 'exercises'), ('t', 'tutorial')], max_length=1)),
            ],
            bases=('portfolio.activity',),
        ),
    ]
