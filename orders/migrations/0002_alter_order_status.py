# Generated by Django 3.2.5 on 2021-08-10 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('New', 'New'), ('Cancelled', 'Cancelled'), ('Accepted', 'Accepted')], default='New', max_length=10),
        ),
    ]
