# Generated by Django 2.0.3 on 2018-04-25 21:06

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ge1', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('tipo', models.SmallIntegerField(choices=[(1, 'Plan de desarrollo'), (2, 'Sistema de salud'), (3, 'Sistema de gestion'), (4, 'Financiero'), (5, 'Otro')], default=1)),
                ('consecutivo', models.IntegerField()),
                ('nombre_identificador', models.CharField(blank=True, max_length=300, null=True)),
                ('objetivo', models.TextField(blank=True, null=True)),
                ('producto_mide', models.TextField(blank=True, null=True)),
                ('tipo_medicion', models.SmallIntegerField(choices=[(1, 'Manual'), (2, 'Automatico')], default=1)),
                ('ciclo', models.SmallIntegerField(choices=[(1, 'Anual'), (2, 'Bienal'), (3, 'Trienal'), (4, 'Cuatrienal'), (5, 'Quinquenal'), (10, 'Decenal')], default=12)),
                ('periodicidad', models.SmallIntegerField(choices=[(1, 'Diario'), (2, 'Semanal'), (3, 'Quincenal'), (4, 'Mensual'), (5, 'Bimensual'), (6, 'Trimestral'), (7, 'Cuatrimestral'), (8, 'Semestral'), (9, 'Anual'), (10, 'Bienal'), (11, 'Trienal'), (12, 'Cuatrienal'), (13, 'Otro')], default=8)),
                ('ambito', models.SmallIntegerField(choices=[(1, 'Impacto'), (2, 'Gestion'), (3, 'Resultado'), (4, 'Proceso'), (5, 'Producto'), (6, 'Efecto'), (7, 'Accion'), (8, 'Recurso')], default=3)),
                ('dimension', models.SmallIntegerField(choices=[(1, 'Eficacia'), (2, 'Eficiencia'), (3, 'Efectividad'), (4, 'Economia'), (5, 'Seguridad'), (6, 'Calidad'), (7, 'Atencion'), (8, 'Equidad')], default=1)),
                ('normatividad', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Resolucion 256'), (2, 'Resolucion 743'), (3, 'Decreto 2193'), (4, 'Resolución 1552'), (5, 'Circular 030')], max_length=10)),
                ('fecha_registro', models.DateTimeField(editable=False)),
                ('fecha_modificacion', models.DateTimeField()),
                ('fecha_actualizacion', models.DateTimeField()),
                ('limite_reporte', models.SmallIntegerField(choices=[(1, 'Primero día hábil del siguiente periodo'), (2, 'Segundo día hábil del siguiente periodo'), (3, 'Tercero día hábil del siguiente periodo'), (4, 'Cuarto día hábil del siguiente periodo'), (5, 'Quinto día hábil del siguiente periodo'), (6, 'Sexto día hábil del siguiente periodo'), (7, 'Septimo día hábil del siguiente periodo'), (8, 'Octavo día hábil del siguiente periodo'), (9, 'Noveno día hábil del siguiente periodo'), (10, 'Decimo día hábil del siguiente periodo'), (15, 'Día quince del siguiente periodo'), (20, 'Día veinte del siguiente periodo'), (25, 'Día veinti cinco del siguiente periodo'), (28, 'Día ultimo dia mes del siguiente periodo')], default=2)),
                ('version', models.FloatField(default='1')),
                ('recurrencia', models.NullBooleanField(default=True)),
                ('verificado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('indicador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tableroMando.Indicador')),
                ('tipo_formula', models.SmallIntegerField(choices=[(1, 'Porcentaje'), (2, 'Tasa de variación'), (3, 'Promedio'), (4, 'Numero entero')], default=2)),
                ('unidad_medicion', models.SmallIntegerField(choices=[(1, 'Porcentaje')], default=1)),
                ('tendencia', models.SmallIntegerField(choices=[(1, 'Incremento'), (2, 'Mantenimiento'), (3, 'Disminucion')], default=1)),
                ('archivo_asociado', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre_variable_1', models.CharField(max_length=200)),
                ('nomenclaruta_1', models.CharField(max_length=6)),
                ('unidad_1', models.SmallIntegerField(blank=True, choices=[(1, 'Porcentaje')], null=True)),
                ('fuente_1', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre_variable_2', models.CharField(blank=True, max_length=200, null=True)),
                ('nomenclaruta_2', models.CharField(blank=True, max_length=6, null=True)),
                ('unidad_2', models.SmallIntegerField(blank=True, choices=[(1, 'Porcentaje')], null=True)),
                ('fuente_2', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre_respuesta', models.CharField(blank=True, max_length=200, null=True)),
                ('nomenclaruta_respuesta', models.CharField(blank=True, max_length=6, null=True)),
                ('unidad_respuesta', models.SmallIntegerField(blank=True, choices=[(1, 'Porcentaje')], null=True)),
                ('fuente_respuesta', models.CharField(blank=True, max_length=100, null=True)),
                ('formula', models.TextField()),
                ('interpretacion_resultado', models.TextField(blank=True, null=True)),
                ('rango_inicial', models.IntegerField(blank=True, null=True)),
                ('rango_final', models.IntegerField(blank=True, null=True)),
                ('responsable_reporte', models.SmallIntegerField(blank=True, choices=[(1, 'Gerente'), (2, 'Subgerente administrativo'), (3, 'Subgerente cientifico'), (4, 'Coordinador 1'), (5, 'Coordinador 2'), (6, 'Coordinador 3')], null=True)),
                ('responsable_consolidacion', models.SmallIntegerField(blank=True, choices=[(1, 'Gerente'), (2, 'Subgerente administrativo'), (3, 'Subgerente cientifico'), (4, 'Coordinador 1'), (5, 'Coordinador 2'), (6, 'Coordinador 3')], null=True)),
                ('responsable_analisis_seguimiento', models.SmallIntegerField(blank=True, choices=[(1, 'Gerente'), (2, 'Subgerente administrativo'), (3, 'Subgerente cientifico'), (4, 'Coordinador 1'), (5, 'Coordinador 2'), (6, 'Coordinador 3')], null=True)),
                ('responsable_decisiones', models.SmallIntegerField(blank=True, choices=[(1, 'Gerente'), (2, 'Subgerente administrativo'), (3, 'Subgerente cientifico'), (4, 'Coordinador 1'), (5, 'Coordinador 2'), (6, 'Coordinador 3')], null=True)),
            ],
        ),
        migrations.AddField(
            model_name='indicador',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ge1.SisCargos'),
        ),
    ]
