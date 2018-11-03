# Generated by Django 2.1.3 on 2018-11-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('valor_diaria', models.DecimalField(decimal_places=2, default=100.0, max_digits=6)),
            ],
        ),
    ]