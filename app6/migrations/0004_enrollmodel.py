# Generated by Django 3.0.5 on 2020-07-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app6', '0003_auto_20200714_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollModel',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('coursename', models.CharField(max_length=50, unique=True)),
                ('facultyname', models.CharField(max_length=50)),
                ('fees', models.FloatField()),
                ('stardate', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('classtime', models.TimeField()),
            ],
        ),
    ]
