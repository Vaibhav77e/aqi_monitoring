# Generated by Django 4.1.4 on 2023-02-19 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0002_testing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance_details',
            fields=[
                ('sl_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('student_id', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Student_details',
            fields=[
                ('student_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('usn', models.CharField(max_length=10)),
                ('phonenum', models.IntegerField()),
            ],
        ),
    ]
