# Generated by Django 4.2.6 on 2023-10-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_answer_image_quiz_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='answer_images/'),
        ),
    ]
