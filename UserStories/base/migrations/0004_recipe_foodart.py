# Generated by Django 3.2.24 on 2024-02-21 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20240221_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='foodart',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
