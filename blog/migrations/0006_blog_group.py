# Generated by Django 3.2.4 on 2021-06-24 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.group'),
        ),
    ]
