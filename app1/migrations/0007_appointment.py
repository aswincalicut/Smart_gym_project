# Generated by Django 4.1.7 on 2023-06-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_bill_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
    ]
