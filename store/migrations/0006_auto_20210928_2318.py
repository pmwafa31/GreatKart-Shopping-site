# Generated by Django 3.1 on 2021-09-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_reviewrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewrating',
            name='review',
        ),
        migrations.AddField(
            model_name='reviewrating',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='subject',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
