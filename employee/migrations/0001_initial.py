# Generated by Django 4.2.13 on 2024-05-28 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('unemployment_duration', models.CharField(max_length=100)),
            ],
            options={
                'unique_together': {('name', 'gender', 'age', 'education', 'unemployment_duration')},
            },
        ),
        migrations.CreateModel(
            name='employee_identity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(blank=True, max_length=100, null=True)),
                ('employee_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='employee_current',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_status', models.CharField(blank=True, max_length=100, null=True)),
                ('employee_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]
