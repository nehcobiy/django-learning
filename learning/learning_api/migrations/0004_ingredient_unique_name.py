# Generated by Django 4.2.1 on 2023-06-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_api', '0003_remove_recipe_ingredient1_remove_recipe_ingredient2_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='ingredient',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_name'),
        ),
    ]