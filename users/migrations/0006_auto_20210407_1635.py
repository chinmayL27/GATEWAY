# Generated by Django 3.1.3 on 2021-04-07 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_resident_visible'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resident',
            options={'ordering': ['-flatNo']},
        ),
    ]