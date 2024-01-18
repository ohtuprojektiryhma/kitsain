# Generated by Django 5.0.1 on 2024-01-18 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(
                    blank=True, default='', max_length=100)),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                 related_name='ingredients', to='backend.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.CharField(blank=True, default='', max_length=1000)),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                 related_name='steps', to='backend.recipe')),
            ],
        ),
    ]
