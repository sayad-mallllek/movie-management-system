# Generated by Django 4.1.6 on 2023-02-11 22:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0005_alter_movie_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="purchase_price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="movie",
            name="rental_price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]