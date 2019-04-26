# Generated by Django 2.2 on 2019-04-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('title_field', models.CharField(max_length=30)),
                ('date_field', models.DateField(auto_now=True)),
                ('step_one', models.CharField(max_length=255)),
                ('step_two', models.CharField(max_length=255)),
                ('step_three', models.CharField(max_length=255)),
                ('step_four', models.CharField(max_length=255)),
                ('step_five', models.CharField(max_length=255)),
                ('completion_percent', models.FloatField()),
            ],
        ),
    ]
