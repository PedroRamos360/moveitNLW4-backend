# Generated by Django 3.1.7 on 2021-04-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='anonymous', max_length=30, unique=True)),
                ('level', models.IntegerField(default=1)),
                ('xp', models.IntegerField(default=0)),
                ('completed_challenges', models.IntegerField(default=0)),
            ],
        ),
    ]
