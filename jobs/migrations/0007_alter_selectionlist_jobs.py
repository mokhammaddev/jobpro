# Generated by Django 4.2 on 2023-05-05 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_selectionlist_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectionlist',
            name='jobs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobs', unique=True),
        ),
    ]
