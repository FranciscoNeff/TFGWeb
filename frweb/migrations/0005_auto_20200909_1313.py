# Generated by Django 3.0.5 on 2020-09-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frweb', '0004_reconocidos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fotos', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.AlterModelOptions(
            name='reconocidos',
            options={'verbose_name': 'Reconocidos', 'verbose_name_plural': 'Reconocidos'},
        ),
    ]
