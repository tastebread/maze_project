# Generated by Django 5.1.5 on 2025-02-04 06:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('question', models.TextField()),
                ('answer', models.CharField(max_length=100)),
                ('hint', models.TextField(blank=True, null=True)),
                ('next_puzzle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.puzzle')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('current_puzzle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.puzzle')),
            ],
        ),
    ]
