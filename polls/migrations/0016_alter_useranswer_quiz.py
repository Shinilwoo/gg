# Generated by Django 4.2.6 on 2023-11-15 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_alter_useranswer_quiz_alter_useranswer_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='useranswer', to='polls.quiz'),
        ),
    ]
