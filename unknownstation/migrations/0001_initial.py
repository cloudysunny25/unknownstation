# Generated by Django 2.1.2 on 2018-12-15 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('changed_date', models.DateTimeField(auto_now=True, verbose_name='changed_date')),
                ('blogname', models.CharField(max_length=200)),
                ('intro', models.CharField(max_length=1000)),
                ('domain', models.CharField(blank=True, max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('changed_date', models.DateTimeField(auto_now=True, verbose_name='changed_date')),
                ('name', models.CharField(max_length=50)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unknownstation.Blog')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('changed_date', models.DateTimeField(auto_now=True, verbose_name='changed_date')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('changed_date', models.DateTimeField(auto_now=True, verbose_name='changed_date')),
                ('title', models.CharField(max_length=500)),
                ('content', markdownx.models.MarkdownxField()),
                ('hit', models.IntegerField(default=0)),
                ('published', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unknownstation.Blog')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unknownstation.Category')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='unknownstation.Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
