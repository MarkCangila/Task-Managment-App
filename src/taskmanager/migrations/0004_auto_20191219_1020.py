# Generated by Django 2.2.6 on 2019-12-19 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0003_auto_20191219_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='created_tasks', to='taskmanager.User'),
            preserve_default=False,
        ),
    ]