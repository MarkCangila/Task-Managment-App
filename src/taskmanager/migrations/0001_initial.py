# Generated by Django 2.2.6 on 2019-11-21 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('controllingRole', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taskmanager.Role')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('roles', models.ManyToManyField(to='taskmanager.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('description', models.CharField(max_length=1000000000)),
                ('priority', models.IntegerField()),
                ('larger_goal', models.CharField(max_length=10000, null=True)),
                ('estimate_end_date', models.DateField()),
                ('claimants', models.ManyToManyField(related_name='claimed_tasks', to='taskmanager.User')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_tasks', to='taskmanager.User')),
                ('task_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmanager.List')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=1000000000000)),
                ('poster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taskmanager.User')),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='can_add',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='addable_lists', to='taskmanager.Role'),
        ),
        migrations.AddField(
            model_name='list',
            name='can_claim',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='claimable_lists', to='taskmanager.Role'),
        ),
        migrations.AddField(
            model_name='list',
            name='can_read',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='viewable_lists', to='taskmanager.Role'),
        ),
    ]
