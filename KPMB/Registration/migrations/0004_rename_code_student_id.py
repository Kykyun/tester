# Generated by Django 4.1.4 on 2022-12-23 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_alter_student_address_alter_student_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='code',
            new_name='id',
        ),
    ]