# Generated by Django 4.2.2 on 2023-07-07 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaweb', '0008_remove_detalle_boleta_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tiendaweb_usuario',
            },
        ),
    ]
