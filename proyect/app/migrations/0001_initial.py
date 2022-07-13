# Generated by Django 4.0.5 on 2022-07-13 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('nivel_id', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('user_type', models.IntegerField(default=1)),
                ('token_user', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('appelidoP', models.CharField(max_length=50)),
                ('appelidoM', models.CharField(max_length=50)),
                ('materias', models.JSONField(default=None)),
                ('nivel', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.nivel')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]