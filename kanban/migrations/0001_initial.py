# Generated by Django 5.0.1 on 2025-04-16 08:56

import colorfield.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_boards', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, related_name='member_boards', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='accounts.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.IntegerField(default=0)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='kanban.board')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('position', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('urgent', 'Urgent')], default='medium', max_length=10)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL)),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='kanban.column')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='kanban.task')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TaskActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('created', 'Created'), ('moved', 'Moved'), ('assigned', 'Assigned'), ('updated', 'Updated'), ('commented', 'Commented'), ('label_added', 'Label Added'), ('label_removed', 'Label Removed')], max_length=20)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='kanban.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Task Activities',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TaskLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', colorfield.fields.ColorField(default='#FF5733', image_field=None, max_length=25, samples=None)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='kanban.board')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='kanban.tasklabel'),
        ),
    ]
