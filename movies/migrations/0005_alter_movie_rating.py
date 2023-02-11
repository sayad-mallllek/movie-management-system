# Generated by Django 4.1.6 on 2023-02-11 22:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0004_remove_movie_display_times_alter_movie_runtime_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="rating",
            field=models.FloatField(
                default=0.0,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(10.0),
                ],
            ),
        ),
    ]