# Generated by Django 2.0.3 on 2018-04-28 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tableroMando', '0002_auto_20180425_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicion',
            name='unidad_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ge1.SisUnidadesMedida'),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='unidad_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ge1.SisUnidadesMedida'),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='unidad_medicion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ge1.SisUnidadesMedida'),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='unidad_respuesta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ge1.SisUnidadesMedida'),
        ),
    ]