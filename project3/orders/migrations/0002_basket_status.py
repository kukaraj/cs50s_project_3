# Generated by Django 2.2 on 2019-04-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='status',
            field=models.CharField(max_length=64, null=True),
        ),
    ]