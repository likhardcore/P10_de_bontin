# Generated by Django 4.0 on 2021-12-23 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_contributor_user_alter_project_contributor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Project', to='api.project'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='role',
            field=models.CharField(choices=[('CON', 'Contribotor'), ('AUTH', 'Author')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='api.user'),
        ),
    ]
