# Generated by Django 2.1.2 on 2018-12-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unknownstation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='content_markdown',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]