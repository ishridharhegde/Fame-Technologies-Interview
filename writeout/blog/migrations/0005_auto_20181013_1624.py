# Generated by Django 2.0.6 on 2018-10-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_employeeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='employeeID',
            field=models.IntegerField(default='100'),
        ),
    ]