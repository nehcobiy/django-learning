# Generated by Django 4.2.1 on 2023-06-21 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_api', '0004_ingredient_unique_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient1',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient2',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient1',
            field=models.ManyToManyField(blank=True, null=True, related_name='i1', to='learning_api.ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient2',
            field=models.ManyToManyField(blank=True, null=True, related_name='i2', to='learning_api.ingredient'),
        ),
    ]
