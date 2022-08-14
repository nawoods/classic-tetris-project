# Generated by Django 3.2.11 on 2022-07-26 19:08

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classic_tetris_project', '0072_remove_tournament_bracket_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='bracket_color',
            field=colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True),
        ),
    ]