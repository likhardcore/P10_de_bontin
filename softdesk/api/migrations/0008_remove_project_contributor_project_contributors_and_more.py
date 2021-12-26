# Generated by Django 4.0 on 2021-12-24 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_contributor_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='contributor',
        ),
        migrations.AddField(
            model_name='project',
            name='contributors',
            field=models.ManyToManyField(related_name='contribution', through='api.Contributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contributor',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
            preserve_default=False,
        ),
    ]