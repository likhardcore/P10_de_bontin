# Generated by Django 4.0 on 2021-12-26 03:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_project_contributor_project_contributors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(default=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Initiator', to=settings.AUTH_USER_MODEL), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Assignee', to='api.user'),
        ),
    ]
