# Generated by Django 4.0.5 on 2023-01-17 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractnewtext',
            name='postDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 17, 21, 27, 1, 927200)),
        ),
    ]
