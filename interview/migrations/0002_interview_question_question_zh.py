# Generated by Django 4.1.13 on 2024-07-18 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview_question',
            name='question_zh',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]