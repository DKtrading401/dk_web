# Generated by Django 5.1.4 on 2025-01-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_title', models.CharField(max_length=50)),
                ('board_writer', models.CharField(max_length=30)),
                ('board_content', models.TextField()),
                ('board_regdate', models.DateTimeField(auto_now=True)),
                ('board_readcount', models.IntegerField(default=0)),
            ],
        ),
    ]