# Generated by Django 2.1.5 on 2020-04-17 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app04', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('content', models.CharField(max_length=400, verbose_name='内容')),
            ],
        ),
    ]
