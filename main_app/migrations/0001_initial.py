# Generated by Django 2.0.13 on 2019-04-08 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fatherName', models.CharField(max_length=50)),
                ('motherName', models.CharField(max_length=50)),
                ('fatherCell', models.CharField(max_length=20)),
                ('fatherEmail', models.CharField(max_length=50)),
                ('motherCell', models.CharField(max_length=20)),
                ('motherEmail', models.CharField(max_length=50)),
                ('presentAddress', models.CharField(max_length=200)),
                ('permanentAddress', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('dateOfBirth', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('studentId', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='parents',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Student'),
        ),
    ]
