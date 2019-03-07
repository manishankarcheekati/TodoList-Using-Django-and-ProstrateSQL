from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default=b'09 28, 2017'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default=b'09 28, 2017'),
        ),
    ]
