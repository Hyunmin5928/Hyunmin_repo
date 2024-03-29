# Generated by Django 4.2.2 on 2023-06-27 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('b_no', models.AutoField(db_column='b_no', primary_key=True, serialize=False)),
                ('b_title', models.CharField(db_column='b_title', max_length=255)),
                ('b_note', models.TextField(db_column='b_note')),
                ('b_writer', models.CharField(db_column='b_writer', max_length=50)),
                ('parent_no', models.IntegerField(db_column='parent_no', default=0)),
                ('b_count', models.IntegerField(db_column='b_count', default=0)),
                ('b_date', models.DateTimeField(db_column='b_date')),
            ],
            options={
                'db_table': 'board',
                'managed': False,
            },
        ),
    ]
