# Generated by Django 4.2.7 on 2023-11-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(default=50),
        ),
    ]
