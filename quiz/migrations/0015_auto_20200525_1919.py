# Generated by Django 2.1.4 on 2020-05-25 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_auto_20200525_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='quizname',
            field=models.CharField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('Django', 'Django'), ('Javascript', 'Javascript'), ('VueJS', 'VueJS')], default='Quiz', max_length=50),
        ),
    ]
