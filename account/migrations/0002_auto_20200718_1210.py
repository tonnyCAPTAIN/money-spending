# Generated by Django 3.0.6 on 2020-07-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='civil_servant',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='not_civil_servant',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]