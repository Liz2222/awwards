# Generated by Django 4.0.5 on 2022-06-12 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('projects', '0004_rename_project_url_project_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='voters',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('usability', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('content', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('design_average', models.FloatField(default=0)),
                ('usability_average', models.FloatField(default=0)),
                ('content_average', models.FloatField(default=0)),
                ('average_rating', models.FloatField(default=0)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='projects.project')),
                ('rater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
