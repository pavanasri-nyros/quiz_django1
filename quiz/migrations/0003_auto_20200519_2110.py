# Generated by Django 2.1.4 on 2020-05-19 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_html2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='html2',
            old_name='correct_answer',
            new_name='answer',
        ),
    ]