# Generated by Django 5.0.3 on 2024-03-14 17:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0004_rename_authors_quote_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='author',
        ),
        migrations.AddField(
            model_name='quote',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quoteapp.author'),
            preserve_default=False,
        ),
    ]
