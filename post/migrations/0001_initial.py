# Generated by Django 3.2.2 on 2021-05-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', '남자'), ('female', '여자')], max_length=6)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]