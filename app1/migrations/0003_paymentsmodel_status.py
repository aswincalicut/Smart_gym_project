# Generated by Django 4.1.7 on 2023-05-16 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_creditcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentsmodel',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
