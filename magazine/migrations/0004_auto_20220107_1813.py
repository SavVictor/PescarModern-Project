# Generated by Django 3.2.9 on 2022-01-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_auto_20211206_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazine',
            name='pdf_file',
        ),
        migrations.AddField(
            model_name='magazine',
            name='featured',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Prima Pagina'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Titlu'),
        ),
    ]