# Generated by Django 2.0.5 on 2018-07-05 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20180705_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='pending_tickets',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
