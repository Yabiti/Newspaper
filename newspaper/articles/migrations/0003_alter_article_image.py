# Generated by Django 5.1.5 on 2025-02-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='images/default.jpg', upload_to='images/'),
        ),
    ]
