# Generated by Django 5.1.2 on 2025-02-18 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='capa',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
