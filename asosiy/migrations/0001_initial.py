# Generated by Django 4.2 on 2023-05-16 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Togri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('togri', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notogri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notogri', models.CharField(max_length=100)),
                ('t_soz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.togri')),
            ],
        ),
    ]
