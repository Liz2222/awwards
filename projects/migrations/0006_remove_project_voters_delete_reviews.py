# Generated by Django 4.0.5 on 2022-06-12 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_voters_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='voters',
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]