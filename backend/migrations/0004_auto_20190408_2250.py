# Generated by Django 2.1.7 on 2019-04-08 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_course_questiontemplate_quiz_quizlog_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='hashes_json',
        ),
        migrations.AddField(
            model_name='student',
            name='course_id',
            field=models.IntegerField(null=True),
        ),
    ]
