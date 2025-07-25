# Generated by Django 5.2.3 on 2025-06-24 12:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('severity', models.CharField(choices=[('minor', 'Minor'), ('moderate', 'Moderate'), ('severe', 'Severe')], default='minor', max_length=20)),
                ('severity_score', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='pending', max_length=20)),
                ('assigned_hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospital_accidents', to=settings.AUTH_USER_MODEL)),
                ('assigned_police', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='police_accidents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
