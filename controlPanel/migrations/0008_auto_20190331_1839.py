# Generated by Django 2.1.7 on 2019-03-31 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controlPanel', '0007_quiz_is_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questiontemplate',
            old_name='hashes_json',
            new_name='template_json',
        ),
    ]
