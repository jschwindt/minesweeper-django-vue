# Generated by Django 2.2.5 on 2019-09-17 02:43

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'new'), ('play', 'playing'), ('pause', 'paused'), ('won', 'won'), ('lost', 'lost')], default='new', max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('time_taken', models.IntegerField(default=0)),
                ('board_rows', models.IntegerField(default=9)),
                ('board_cols', models.IntegerField(default=9)),
                ('board_bombs', models.IntegerField(default=10)),
                ('board', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
