# Generated by Django 4.2.3 on 2023-08-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('start_date', models.DateField(max_length=100)),
                ('fee', models.IntegerField()),
                ('timings', models.CharField(max_length=100)),
                ('trainer_name', models.CharField(max_length=100)),
                ('trainer_exp', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000)),
                ('date', models.DateField(max_length=100)),
            ],
        ),
    ]
