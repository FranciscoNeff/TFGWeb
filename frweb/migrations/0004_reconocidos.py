# Generated by Django 3.0.5 on 2020-09-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frweb', '0003_subirvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reconocidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Reconocidos',
            },
        ),
    ]
