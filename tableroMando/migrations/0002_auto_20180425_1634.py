# Generated by Django 2.0.3 on 2018-04-25 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tableroMando', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicion',
            name='responsable_analisis_seguimiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ge1.SisCargos'),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='responsable_consolidacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ge1.SisCargos'),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='responsable_decisiones',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ge1.SisCargos'),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='responsable_reporte',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ge1.SisCargos'),
        ),
    ]