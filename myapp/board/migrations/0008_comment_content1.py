# Generated by Django 4.0.6 on 2022-08-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_question_view_cnt_questioncount'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content1',
            field=models.TextField(null=True),
        ),
    ]
