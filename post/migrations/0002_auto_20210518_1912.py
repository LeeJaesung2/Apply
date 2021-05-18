# Generated by Django 3.2.2 on 2021-05-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_img'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='gender',
            field=models.CharField(choices=[('남자', '남자'), ('여자', '여자')], max_length=6),
        ),
    ]
