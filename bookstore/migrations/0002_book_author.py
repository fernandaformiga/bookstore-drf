# Generated by Django 3.2.4 on 2021-06-16 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='bookstore.Author'),
        ),
    ]
