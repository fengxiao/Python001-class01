# Generated by Django 2.2.13 on 2020-08-02 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T2',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('n_star', models.IntegerField()),
                ('short', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 't2',
                'managed': True,
            },
        ),
    ]
