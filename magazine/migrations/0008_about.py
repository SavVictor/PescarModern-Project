# Generated by Django 3.2.9 on 2022-01-07 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0007_alter_magazine_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Titlu')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Paragraf')),
                ('image', models.ImageField(default='images/default.png', help_text='Atașează o poză pentru paragraf', upload_to='img/', verbose_name='Imagine')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
    ]
