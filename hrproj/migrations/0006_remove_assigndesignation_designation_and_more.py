# Generated by Django 5.0.3 on 2024-03-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrproj', '0005_department_designation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assigndesignation',
            name='designation',
        ),
        migrations.AddField(
            model_name='assigndesignation',
            name='designation_id',
            field=models.CharField(default='DEFAULT_VALUE', max_length=100),
        ),
    ]