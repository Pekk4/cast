# Generated by Django 4.1.5 on 2023-03-13 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.TextField(null=True)),
                ('certificate_name', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_tech_skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_level', models.IntegerField(choices=[(1, 'Wants To Learn'), (2, 'Can Work With'), (3, 'Proficient')])),
                ('tech_preference', models.BooleanField(null=True)),
            ],
            options={
                'ordering': ['tech'],
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.TextField(unique=True)),
                ('phone_number', models.TextField(null=True)),
                ('location_country', models.TextField(null=True)),
                ('location_city', models.TextField(null=True)),
                ('worktime_allocation', models.IntegerField(null=True)),
                ('allocation_until', models.DateField(null=True)),
                ('wants_to_do', models.TextField(null=True)),
                ('wants_not_to_do', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Techs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_name', models.TextField(unique=True)),
                ('employee', models.ManyToManyField(through='restapi.Employee_tech_skills', to='restapi.employees')),
            ],
        ),
        migrations.AddField(
            model_name='employee_tech_skills',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='restapi.employees'),
        ),
        migrations.AddField(
            model_name='employee_tech_skills',
            name='tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tech', to='restapi.techs'),
        ),
        migrations.CreateModel(
            name='Employee_certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_until', models.DateField(null=True)),
                ('cert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cert', to='restapi.certificate')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='restapi.employees')),
            ],
            options={
                'ordering': ['cert'],
            },
        ),
        migrations.AddField(
            model_name='certificate',
            name='employee',
            field=models.ManyToManyField(through='restapi.Employee_certificates', to='restapi.employees'),
        ),
    ]
