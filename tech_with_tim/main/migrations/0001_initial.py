# Generated by Django 3.2.8 on 2022-04-18 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('surname', models.CharField(max_length=255, verbose_name='Surname')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone')),
                ('theme', models.CharField(max_length=255, verbose_name='Theme')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255, verbose_name='Course name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('about', models.TextField(verbose_name='About')),
                ('contact', models.CharField(max_length=255, verbose_name='Contact')),
                ('image', models.ImageField(upload_to='', verbose_name='Choose image main (format: jpg, jpeg, png)')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Question')),
                ('answer', models.CharField(max_length=255, verbose_name='Answer')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photo/%y/%m/%d', verbose_name='Choose image main (format: jpg, jpeg, png)')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=255, verbose_name='Teacher name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('about', models.TextField(verbose_name='About')),
                ('contact', models.CharField(max_length=255, verbose_name='Contact')),
                ('social_networks', models.CharField(max_length=255, verbose_name='Social networks')),
                ('image', models.ImageField(upload_to='photo/%y/%m/%d', verbose_name='Choose image main (format: jpg, jpeg, png)')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
