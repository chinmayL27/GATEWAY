# Generated by Django 3.1.3 on 2021-04-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210402_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='flatNo',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]