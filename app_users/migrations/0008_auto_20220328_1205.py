# Generated by Django 3.1.1 on 2022-03-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0007_auto_20220328_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_type',
            field=models.CharField(choices=[('teacher', 'teacher'), ('student', 'student')], default='student', max_length=10),
        ),
    ]
