# Generated by Django 3.0.3 on 2020-02-04 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=1000)),
                ('password', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
