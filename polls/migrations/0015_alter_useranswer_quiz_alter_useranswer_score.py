# Generated by Django 4.2.6 on 2023-11-15 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_alter_useranswer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.quiz'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
