# Generated by Django 4.0.1 on 2022-01-16 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hrms', '0002_alter_attendance_dat_alter_attendance_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Salary',
        ),
    ]