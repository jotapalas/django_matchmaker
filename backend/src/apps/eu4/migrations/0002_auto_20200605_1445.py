# Generated by Django 3.0.6 on 2020-06-05 14:45

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eu4', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eu4matchcontender',
            options={'verbose_name': 'contender', 'verbose_name_plural': 'contenders'},
        ),
        migrations.AlterModelOptions(
            name='eu4tournamentcontender',
            options={'verbose_name': 'contender', 'verbose_name_plural': 'contenders'},
        ),
        migrations.AddField(
            model_name='eu4tournament',
            name='schedule',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='eu4tournamentcontender',
            name='preferred_countries',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=4), default=list, size=None, blank=True),
        ),
        migrations.AlterField(
            model_name='eu4match',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches', to='eu4.EU4Tournament'),
        ),
    ]
