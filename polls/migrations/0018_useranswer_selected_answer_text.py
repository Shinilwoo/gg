# Generated by Django 4.2.6 on 2023-11-30 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_quiz_is_date_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='selected_answer_text',
            field=models.TextField(blank=True),
        ),
    ]