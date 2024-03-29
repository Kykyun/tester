# Generated by Django 4.1.4 on 2022-12-23 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('code', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=12)),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.course')),
            ],
        ),
    ]
