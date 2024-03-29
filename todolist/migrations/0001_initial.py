from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 9, 27, 4, 28, 14, 690000, tzinfo=utc))),
                ('due_date', models.DateField(default=b'09 27, 2017')),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='todolist.Category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
