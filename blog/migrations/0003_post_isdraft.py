# Generated by Django 4.2.5 on 2023-10-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_created_post_published_date_post_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isDraft',
            field=models.BooleanField(default=True),
        ),
    ]
