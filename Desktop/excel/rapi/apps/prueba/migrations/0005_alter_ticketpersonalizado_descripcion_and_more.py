# Generated by Django 5.0.1 on 2024-01-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0004_alter_registartpagonaranja_telefono_titular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketpersonalizado',
            name='descripcion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ticketpersonalizado',
            name='descripcion_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ticketpersonalizado',
            name='descripcion_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ticketpersonalizado',
            name='descripcion_4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ticketpersonalizado',
            name='detalle_descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ticketpersonalizado',
            name='detalle_descripcion_2',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ticketpersonalizado',
            name='detalle_descripcion_3',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ticketpersonalizado',
            name='detalle_descripcion_4',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ticketpersonalizado',
            name='ingresar_empresa',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='ticketpersonalizado',
            name='ingresar_fecha',
            field=models.DateField(default='2000-01-01', null=True),
        ),
        migrations.AlterField(
            model_name='ticketpersonalizado',
            name='ingresar_hora',
            field=models.TimeField(default='00:00', null=True),
        ),
        migrations.AlterField(
            model_name='ticketpersonalizado',
            name='ingresar_importe',
            field=models.FloatField(null=True),
        ),
    ]