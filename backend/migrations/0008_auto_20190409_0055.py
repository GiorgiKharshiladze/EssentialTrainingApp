# Generated by Django 2.1.7 on 2019-04-09 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_course_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='course_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='course_id',
            field=models.IntegerField(null=True),
        ),
    ]
