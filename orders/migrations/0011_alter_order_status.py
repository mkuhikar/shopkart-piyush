# Generated by Django 3.2.5 on 2021-08-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='New', max_length=10),
        ),
    ]
