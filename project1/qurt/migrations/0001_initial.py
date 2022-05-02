# Generated by Django 4.0.2 on 2022-03-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameoftypes', models.CharField(max_length=30)),
                ('prices', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('photosofqurt', models.ImageField(null=True, upload_to='images/', verbose_name='Фото')),
            ],
        ),
    ]