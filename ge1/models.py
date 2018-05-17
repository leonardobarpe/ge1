# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acumulados(models.Model):
    fecha_cierre = models.DateField(primary_key=True)
    codigo_area = models.DecimalField(max_digits=10, decimal_places=0)
    area_superior = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    solicitudes_recibidas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    solicitudes_atendidas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    solicitudes_noatendidas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    solicitudes_escaladas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    oportunidad_excelente = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    oportunidad_buena = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    oportunidad_regular = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    confiabilidad_excelente = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    confiabilidad_buena = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    confiabilidad_regular = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    indice_oportunidad = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    indice_confiabilidad = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acumulados'
        unique_together = (('fecha_cierre', 'codigo_area'),)


class AcumuladosPersona(models.Model):
    fecha_cierre = models.DateField(primary_key=True)
    codigo_persona = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_area = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    solicitudes_recibidas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    solicitudes_atendidas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    solicitudes_noatendidas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    solicitudes_escaladas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    oportunidad_excelente = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    oportunidad_buena = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    oportunidad_regular = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    confiabilidad_excelente = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    confiabilidad_buena = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    confiabilidad_regular = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    indice_oportunidad = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    indice_confiabilidad = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acumulados_persona'
        unique_together = (('fecha_cierre', 'codigo_persona'),)


class AmAcciones(models.Model):
    numero = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    fecha_generada = models.DateTimeField(blank=True, null=True)
    area_implanta = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    empleado_cliente = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    codigo_estado = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    nivel_escalamiento = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_vigencia = models.DateTimeField(blank=True, null=True)
    fecha_estimada_terminacion = models.DateTimeField(blank=True, null=True)
    fecha_real_terminacion = models.DateTimeField(blank=True, null=True)
    fecha_base_escalamientos = models.DateTimeField(blank=True, null=True)
    accion = models.CharField(max_length=1, blank=True, null=True)
    origen = models.ForeignKey('AmOrigen', models.DO_NOTHING, db_column='origen', blank=True, null=True)
    proceso = models.CharField(max_length=20, blank=True, null=True)
    subproceso = models.CharField(max_length=60, blank=True, null=True)
    numeral = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=4000, blank=True, null=True)
    cumplio = models.CharField(max_length=1, blank=True, null=True)
    implantada = models.CharField(max_length=1, blank=True, null=True)
    revisada_comite = models.CharField(max_length=1, blank=True, null=True)
    funcionario1 = models.CharField(max_length=40, blank=True, null=True)
    cargo1 = models.CharField(max_length=50, blank=True, null=True)
    fecha1 = models.DateTimeField(blank=True, null=True)
    revisada_auditor = models.CharField(max_length=1, blank=True, null=True)
    funcionario2 = models.CharField(max_length=40, blank=True, null=True)
    cargo2 = models.CharField(max_length=50, blank=True, null=True)
    fecha2 = models.DateTimeField(blank=True, null=True)
    norma = models.CharField(max_length=15, blank=True, null=True)
    justificacion = models.CharField(max_length=2000, blank=True, null=True)
    observaciones_cierre = models.CharField(max_length=512, blank=True, null=True)
    observaciones_calidad = models.CharField(max_length=255, blank=True, null=True)
    fecha_calidad = models.DateTimeField(blank=True, null=True)
    tema = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    impacto = models.CharField(max_length=1, blank=True, null=True)
    tema_accion = models.CharField(max_length=60, blank=True, null=True)
    solicitud_origen = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    codigo_ciclo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    codigo_plan = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    codigo_meta = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    asociado = models.CharField(max_length=1, blank=True, null=True)
    vieja = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_acciones'


class AmAccionesAreas(models.Model):
    numero = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    area_implanta = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_acciones_areas'
        unique_together = (('numero', 'area_implanta'),)


class AmArchivos(models.Model):
    numero_solicitud = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    consecutivo = models.DecimalField(max_digits=10, decimal_places=0)
    causa = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    archivo = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_archivos'
        unique_together = (('numero_solicitud', 'consecutivo'),)


class AmCausas(models.Model):
    numero = models.OneToOneField(AmAcciones, models.DO_NOTHING, db_column='numero', primary_key=True)
    consecutivo = models.DecimalField(max_digits=10, decimal_places=0)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    porque = models.CharField(max_length=4000, blank=True, null=True)
    accion = models.CharField(max_length=4000, blank=True, null=True)
    beneficios = models.CharField(max_length=15, blank=True, null=True)
    beneficio = models.CharField(max_length=4000, blank=True, null=True)
    responsable = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_estimada_terminacion = models.DateTimeField(blank=True, null=True)
    fecha_real_terminacion = models.DateTimeField(blank=True, null=True)
    fecha_revision = models.DateTimeField(blank=True, null=True)
    estado = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    prorrogas = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    justificacion = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_causas'
        unique_together = (('numero', 'consecutivo'),)


class AmCausasPeriodo(models.Model):
    periodo = models.CharField(primary_key=True, max_length=6)
    numero = models.DecimalField(max_digits=10, decimal_places=0)
    consecutivo = models.DecimalField(max_digits=10, decimal_places=0)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    porque = models.CharField(max_length=4000, blank=True, null=True)
    accion = models.CharField(max_length=4000, blank=True, null=True)
    beneficios = models.CharField(max_length=15, blank=True, null=True)
    beneficio = models.CharField(max_length=4000, blank=True, null=True)
    responsable = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_estimada_terminacion = models.DateTimeField(blank=True, null=True)
    fecha_real_terminacion = models.DateTimeField(blank=True, null=True)
    fecha_revision = models.DateTimeField(blank=True, null=True)
    estado = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    prorrogas = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    justificacion = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_causas_periodo'
        unique_together = (('periodo', 'numero', 'consecutivo'),)


class AmEstadoCausas(models.Model):
    codigo = models.DecimalField(max_digits=4, decimal_places=0)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_estado_causas'


class AmEstados(models.Model):
    codigo = models.DecimalField(max_digits=4, decimal_places=0)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_estados'


class AmNormas(models.Model):
    norma = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_normas'


class AmNormasNumeral(models.Model):
    norma = models.CharField(primary_key=True, max_length=15)
    numeral = models.CharField(max_length=20)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_normas_numeral'
        unique_together = (('norma', 'numeral'),)


class AmOrigen(models.Model):
    codigo = models.CharField(primary_key=True, max_length=3)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    ver_jefe_area = models.CharField(max_length=1, blank=True, null=True)
    ver_gerencia_calidad = models.CharField(max_length=1, blank=True, null=True)
    ver_otros = models.CharField(max_length=1, blank=True, null=True)
    captura_numeral = models.CharField(max_length=1, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_origen'


class AmOrigenArea(models.Model):
    codigo_origen = models.CharField(primary_key=True, max_length=3)
    codigo_area = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_origen_area'
        unique_together = (('codigo_origen', 'codigo_area'),)


class AmSeguimiento(models.Model):
    numero = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    causa = models.DecimalField(max_digits=10, decimal_places=0)
    consecutivo = models.DecimalField(max_digits=10, decimal_places=0)
    observacion = models.CharField(max_length=512, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    personaatendio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    automatico = models.CharField(max_length=1, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_seguimiento'
        unique_together = (('numero', 'causa', 'consecutivo'),)


class AmTemas(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=1)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_temas'


class AmTipo(models.Model):
    codigo = models.CharField(primary_key=True, max_length=1)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_tipo'


class AmTipoCausa(models.Model):
    tipo = models.CharField(primary_key=True, max_length=1)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'am_tipo_causa'


class AplazamientosSolicitud(models.Model):
    numero_solicitud = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    consecutivo = models.DecimalField(max_digits=10, decimal_places=0)
    justificacion = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    estado = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_estado = models.DateTimeField(blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    justificacion_nega = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aplazamientos_solicitud'
        unique_together = (('numero_solicitud', 'consecutivo'),)


class ArchivoEncuesta(models.Model):
    numero_encuesta = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    archivo = models.CharField(max_length=200, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'archivo_encuesta'


class ArchivosSolicitud(models.Model):
    numero_solicitud = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    consecutivo = models.DecimalField(max_digits=10, decimal_places=0)
    archivo = models.CharField(max_length=200)
    estado = models.CharField(max_length=1, blank=True, null=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'archivos_solicitud'
        unique_together = (('numero_solicitud', 'consecutivo'),)


class AreasAuditadas(models.Model):
    ciclo = models.CharField(primary_key=True, max_length=6)
    area = models.DecimalField(max_digits=10, decimal_places=0)
    persona_auditada = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas_auditadas'
        unique_together = (('ciclo', 'area', 'persona_auditada'),)


class AtencionSolicitud(models.Model):
    numero_solicitud = models.OneToOneField('Solicitudes', models.DO_NOTHING, db_column='numero_solicitud', primary_key=True)
    consecutivo_atencion = models.DecimalField(max_digits=10, decimal_places=0)
    observacion = models.CharField(max_length=1024, blank=True, null=True)
    fecha = models.DateTimeField()
    personaatendio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atencion_solicitud'
        unique_together = (('numero_solicitud', 'consecutivo_atencion'),)


class AudAreasAuditadas(models.Model):
    ciclo = models.ForeignKey('AudPlanAnual', models.DO_NOTHING, db_column='ciclo')
    area = models.ForeignKey('UnidadesDependencia', models.DO_NOTHING, db_column='area')
    codigo_proceso = models.CharField(max_length=20, blank=True, null=True)
    codigo_informe = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    asociado_a = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_areas_auditadas'


class AudBloques(models.Model):
    ciclo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    bloque = models.DecimalField(max_digits=4, decimal_places=0)
    codigo_proceso = models.CharField(max_length=20, blank=True, null=True)
    codigo_informe = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    asociado_a = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_bloques'
        unique_together = (('ciclo', 'bloque'),)


class AudBloquesCriterio(models.Model):
    ciclo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    bloque = models.DecimalField(max_digits=4, decimal_places=0)
    criterio = models.CharField(max_length=10)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_bloques_criterio'
        unique_together = (('ciclo', 'bloque', 'criterio'),)


class AudBloquesPreguntas(models.Model):
    ciclo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    bloque = models.DecimalField(max_digits=4, decimal_places=0)
    pregunta = models.DecimalField(max_digits=4, decimal_places=0)
    descripcion_pregunta = models.CharField(max_length=255)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    ind_conformidad = models.CharField(max_length=1, blank=True, null=True)
    respuesta = models.CharField(max_length=512, blank=True, null=True)
    anotaciones = models.CharField(max_length=2048, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    ind_acciones = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_bloques_preguntas'
        unique_together = (('ciclo', 'bloque', 'pregunta'),)


class AudCriterios(models.Model):
    criterio = models.CharField(primary_key=True, max_length=10)
    descripcion = models.CharField(max_length=100)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_criterios'


class AudGrupoAuditor(models.Model):
    codigo_empleado = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    consecutivo = models.DecimalField(max_digits=6, decimal_places=0)
    rol = models.CharField(max_length=1)
    ciclo = models.DecimalField(max_digits=4, decimal_places=0)
    codigo_proceso = models.CharField(max_length=20, blank=True, null=True)
    codigo_informe = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    asociado_a = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_grupo_auditor'
        unique_together = (('codigo_empleado', 'consecutivo'),)


class AudInformes(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    nombre = models.CharField(max_length=80)
    tipo_informe = models.CharField(max_length=1)
    estrategico = models.CharField(max_length=1, blank=True, null=True)
    misional = models.CharField(max_length=1, blank=True, null=True)
    apoyo = models.CharField(max_length=1, blank=True, null=True)
    evaluacion = models.CharField(max_length=1, blank=True, null=True)
    responsable = models.CharField(max_length=3, blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_informes'


class AudInformesPlanAnual(models.Model):
    ciclo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    codigo_informe = models.DecimalField(max_digits=4, decimal_places=0)
    coordinador_auditoria = models.CharField(max_length=2, blank=True, null=True)
    equipo_auditor = models.CharField(max_length=512, blank=True, null=True)
    mes01 = models.CharField(max_length=1, blank=True, null=True)
    mes02 = models.CharField(max_length=1, blank=True, null=True)
    mes03 = models.CharField(max_length=1, blank=True, null=True)
    mes04 = models.CharField(max_length=1, blank=True, null=True)
    mes05 = models.CharField(max_length=1, blank=True, null=True)
    mes06 = models.CharField(max_length=1, blank=True, null=True)
    mes07 = models.CharField(max_length=1, blank=True, null=True)
    mes08 = models.CharField(max_length=1, blank=True, null=True)
    mes09 = models.CharField(max_length=1, blank=True, null=True)
    mes10 = models.CharField(max_length=1, blank=True, null=True)
    mes11 = models.CharField(max_length=1, blank=True, null=True)
    mes12 = models.CharField(max_length=1, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    area_responsable = models.ForeignKey('UnidadesDependencia', models.DO_NOTHING, db_column='area_responsable', blank=True, null=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    objetivos_especificos = models.TextField(blank=True, null=True)
    alcance = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_informes_plan_anual'
        unique_together = (('ciclo', 'codigo_informe'),)


class AudPlanAnual(models.Model):
    ciclo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    objetivo = models.CharField(max_length=512, blank=True, null=True)
    alcance = models.CharField(max_length=300, blank=True, null=True)
    criterios = models.CharField(max_length=300, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    recursos = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_plan_anual'


class AudProcesosPlanAnual(models.Model):
    ciclo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    codigo_proceso = models.CharField(max_length=20)
    tipo_auditoria = models.CharField(max_length=1)
    coordinador_auditoria = models.CharField(max_length=2)
    equipo_auditor = models.CharField(max_length=512, blank=True, null=True)
    mes01 = models.CharField(max_length=1, blank=True, null=True)
    mes02 = models.CharField(max_length=1, blank=True, null=True)
    mes03 = models.CharField(max_length=1, blank=True, null=True)
    mes04 = models.CharField(max_length=1, blank=True, null=True)
    mes05 = models.CharField(max_length=1, blank=True, null=True)
    mes06 = models.CharField(max_length=1, blank=True, null=True)
    mes07 = models.CharField(max_length=1, blank=True, null=True)
    mes08 = models.CharField(max_length=1, blank=True, null=True)
    mes09 = models.CharField(max_length=1, blank=True, null=True)
    mes10 = models.CharField(max_length=1, blank=True, null=True)
    mes11 = models.CharField(max_length=1, blank=True, null=True)
    mes12 = models.CharField(max_length=1, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    area_responsable = models.ForeignKey('UnidadesDependencia', models.DO_NOTHING, db_column='area_responsable', blank=True, null=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    objetivos_especificos = models.TextField(blank=True, null=True)
    alcance = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aud_procesos_plan_anual'
        unique_together = (('ciclo', 'codigo_proceso'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CalCiclos(models.Model):
    ciclo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    descripcion = models.CharField(max_length=250)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_ciclos'


class CalDocumentos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=20)
    proceso = models.CharField(max_length=20)
    subproceso = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=250)
    version = models.CharField(max_length=30)
    fecha_version = models.CharField(max_length=25)
    url_archivo = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=1)
    tipo_documento = models.CharField(max_length=1, blank=True, null=True)
    nombre_archivo_word = models.CharField(max_length=255, blank=True, null=True)
    nombre_archivo_pdf = models.CharField(max_length=255, blank=True, null=True)
    fecha_emision = models.CharField(max_length=60, blank=True, null=True)
    observaciones = models.CharField(max_length=512, blank=True, null=True)
    orden = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    fecha_revision = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    servicio = models.CharField(max_length=20, blank=True, null=True)
    asociado_a = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_documentos'


class CalDocumentosDistribuido(models.Model):
    codigo_documento = models.CharField(primary_key=True, max_length=20)
    codigo_area = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_documentos_distribuido'
        unique_together = (('codigo_documento', 'codigo_area'),)


class CalDocumentosObjetivo(models.Model):
    codigo_objetivo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    documento = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    procesado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_documentos_objetivo'
        unique_together = (('codigo_objetivo', 'documento'),)


class CalDocumentosResponsables(models.Model):
    codigo_documento = models.CharField(primary_key=True, max_length=20)
    codigo_area = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_documentos_responsables'
        unique_together = (('codigo_documento', 'codigo_area'),)


class CalDocumentosTitulos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=20)
    titulo = models.CharField(max_length=50)
    titulo_padre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=512)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_documentos_titulos'
        unique_together = (('codigo', 'titulo'),)


class CalDocumentosVersiones(models.Model):
    codigo = models.CharField(primary_key=True, max_length=20)
    tipo_documento = models.CharField(max_length=1, blank=True, null=True)
    version = models.CharField(max_length=30)
    fecha_version = models.CharField(max_length=25)
    estado = models.CharField(max_length=1)
    nombre_archivo_word = models.CharField(max_length=255, blank=True, null=True)
    nombre_archivo_pdf = models.CharField(max_length=255, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_documentos_versiones'
        unique_together = (('codigo', 'version'),)


class CalLogros(models.Model):
    codigo_ciclo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    codigo_plan = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_objetivo = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_meta = models.DecimalField(max_digits=10, decimal_places=0)
    periodo = models.DecimalField(max_digits=2, decimal_places=0)
    valor_logro = models.DecimalField(max_digits=21, decimal_places=2)
    valor_meta = models.DecimalField(max_digits=21, decimal_places=2)
    justificacion = models.CharField(max_length=1024, blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    accion_numero = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    oportunidad_excelente = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    oportunidad_buena = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    oportunidad_regular = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    confiabilidad_excelente = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    confiabilidad_buena = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    confiabilidad_regular = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_logros'
        unique_together = (('codigo_ciclo', 'codigo_plan', 'codigo_objetivo', 'codigo_meta', 'periodo'),)


class CalMetas(models.Model):
    codigo_meta = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    codigo_objetivo = models.DecimalField(max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=255)
    justificacion = models.CharField(max_length=255, blank=True, null=True)
    valor_meta = models.DecimalField(max_digits=21, decimal_places=2)
    tipo_medicion = models.CharField(max_length=1)
    frecuencia_medicion = models.CharField(max_length=1, blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    procesado = models.CharField(max_length=1, blank=True, null=True)
    mes01 = models.CharField(max_length=1, blank=True, null=True)
    mes02 = models.CharField(max_length=1, blank=True, null=True)
    mes03 = models.CharField(max_length=1, blank=True, null=True)
    mes04 = models.CharField(max_length=1, blank=True, null=True)
    mes05 = models.CharField(max_length=1, blank=True, null=True)
    mes06 = models.CharField(max_length=1, blank=True, null=True)
    mes07 = models.CharField(max_length=1, blank=True, null=True)
    mes08 = models.CharField(max_length=1, blank=True, null=True)
    mes09 = models.CharField(max_length=1, blank=True, null=True)
    mes10 = models.CharField(max_length=1, blank=True, null=True)
    mes11 = models.CharField(max_length=1, blank=True, null=True)
    mes12 = models.CharField(max_length=1, blank=True, null=True)
    fuente_dato = models.CharField(max_length=15, blank=True, null=True)
    aplica_en = models.CharField(max_length=3, blank=True, null=True)
    unidad_medida = models.CharField(max_length=2, blank=True, null=True)
    valor_minimo = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    valor_maximo = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    tipo_grafica = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_metas'


class CalObjetivos(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    proceso = models.CharField(max_length=20)
    subproceso = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    justificacion = models.CharField(max_length=255, blank=True, null=True)
    tipo_objetivo = models.CharField(max_length=1)
    perspectiva = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    procesado = models.CharField(max_length=1, blank=True, null=True)
    agrega_valor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_objetivos'


class CalPeriodos(models.Model):
    ciclo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    periodo = models.DecimalField(max_digits=2, decimal_places=0)
    descripcion = models.CharField(max_length=250)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_periodos'
        unique_together = (('ciclo', 'periodo'),)


class CalPerspectivas(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=3, decimal_places=0)
    descripcion = models.CharField(max_length=250)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_perspectivas'


class CalPlanDocumentosObjetivo(models.Model):
    codigo_ciclo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    codigo_plan = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_objetivo = models.DecimalField(max_digits=10, decimal_places=0)
    documento = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_plan_documentos_objetivo'
        unique_together = (('codigo_ciclo', 'codigo_plan', 'codigo_objetivo', 'documento'),)


class CalPlanMetas(models.Model):
    codigo_ciclo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    codigo_plan = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_meta = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_objetivo = models.DecimalField(max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=512)
    valor_meta = models.DecimalField(max_digits=21, decimal_places=2)
    tipo_medicion = models.CharField(max_length=1)
    frecuencia_medicion = models.CharField(max_length=1, blank=True, null=True)
    justificacion = models.CharField(max_length=4000, blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    mes01 = models.CharField(max_length=1, blank=True, null=True)
    mes02 = models.CharField(max_length=1, blank=True, null=True)
    mes03 = models.CharField(max_length=1, blank=True, null=True)
    mes04 = models.CharField(max_length=1, blank=True, null=True)
    mes05 = models.CharField(max_length=1, blank=True, null=True)
    mes06 = models.CharField(max_length=1, blank=True, null=True)
    mes07 = models.CharField(max_length=1, blank=True, null=True)
    mes08 = models.CharField(max_length=1, blank=True, null=True)
    mes09 = models.CharField(max_length=1, blank=True, null=True)
    mes10 = models.CharField(max_length=1, blank=True, null=True)
    mes11 = models.CharField(max_length=1, blank=True, null=True)
    mes12 = models.CharField(max_length=1, blank=True, null=True)
    fuente_dato = models.CharField(max_length=15, blank=True, null=True)
    aplica_en = models.CharField(max_length=3, blank=True, null=True)
    unidad_medida = models.CharField(max_length=2, blank=True, null=True)
    valor_minimo = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    valor_maximo = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    tipo_grafica = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_plan_metas'
        unique_together = (('codigo_ciclo', 'codigo_plan', 'codigo_meta'),)


class CalPlanObjetivos(models.Model):
    codigo_ciclo = models.OneToOneField('CalPlanes', models.DO_NOTHING, db_column='codigo_ciclo', primary_key=True)
    codigo_plan = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_objetivo = models.DecimalField(max_digits=10, decimal_places=0)
    proceso = models.CharField(max_length=20)
    subproceso = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=512)
    tipo_objetivo = models.CharField(max_length=1)
    perspectiva = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    estado = models.CharField(max_length=1)
    justificacion = models.CharField(max_length=255, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    agrega_valor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_plan_objetivos'
        unique_together = (('codigo_ciclo', 'codigo_plan', 'codigo_objetivo'),)


class CalPlanRecursosMeta(models.Model):
    codigo_ciclo = models.OneToOneField(CalPlanMetas, models.DO_NOTHING, db_column='codigo_ciclo', primary_key=True)
    codigo_plan = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_meta = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_recurso = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_plan_recursos_meta'
        unique_together = (('codigo_ciclo', 'codigo_plan', 'codigo_meta', 'codigo_recurso'),)


class CalPlanResponsablesMeta(models.Model):
    codigo_ciclo = models.OneToOneField(CalPlanMetas, models.DO_NOTHING, db_column='codigo_ciclo', primary_key=True)
    codigo_plan = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_meta = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_responsable = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_plan_responsables_meta'
        unique_together = (('codigo_ciclo', 'codigo_plan', 'codigo_meta', 'codigo_responsable'),)


class CalPlanes(models.Model):
    ciclo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    codigo_plan = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_area = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    codigo_plantilla = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_planes'
        unique_together = (('ciclo', 'codigo_plan'),)


class CalPlantillas(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    descripcion = models.CharField(max_length=60)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_plantillas'


class CalPlantillasAreas(models.Model):
    codigo_ciclo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    codigo_plantilla = models.ForeignKey(CalPlantillas, models.DO_NOTHING, db_column='codigo_plantilla')
    codigo_area = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    procesado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_plantillas_areas'
        unique_together = (('codigo_ciclo', 'codigo_plantilla', 'codigo_area'),)


class CalPlantillasObjetivos(models.Model):
    codigo_plantilla = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    codigo_objetivo = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    procesado = models.CharField(max_length=1, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_plantillas_objetivos'
        unique_together = (('codigo_plantilla', 'codigo_objetivo'),)


class CalRecursos(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_recursos'


class CalRecursosMeta(models.Model):
    codigo_meta = models.OneToOneField(CalMetas, models.DO_NOTHING, db_column='codigo_meta', primary_key=True)
    codigo_recurso = models.ForeignKey(CalRecursos, models.DO_NOTHING, db_column='codigo_recurso')
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    procesado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_recursos_meta'
        unique_together = (('codigo_meta', 'codigo_recurso'),)


class CalResponsables(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_responsables'


class CalResponsablesMeta(models.Model):
    codigo_meta = models.OneToOneField(CalMetas, models.DO_NOTHING, db_column='codigo_meta', primary_key=True)
    codigo_responsable = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    procesado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_responsables_meta'
        unique_together = (('codigo_meta', 'codigo_responsable'),)


class CalTiposDocumento(models.Model):
    codigo = models.CharField(primary_key=True, max_length=1)
    descripcion = models.CharField(max_length=50)
    mostrar_en_lista_maestra = models.CharField(max_length=1)
    mostrar_en_mapa = models.CharField(max_length=1)
    mostrar_en_planes = models.CharField(max_length=1)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal_tipos_documento'


class Caracteristicas(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=2, blank=True, null=True)
    calificar = models.CharField(max_length=1, blank=True, null=True)
    longitud = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    competencia = models.CharField(max_length=30, blank=True, null=True)
    caracteristica_anida = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    permite_extender = models.CharField(max_length=1, blank=True, null=True)
    caracteristica_depende = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    valor_depende = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tipo_validacion = models.CharField(max_length=2, blank=True, null=True)
    caracteristica_valida = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    nombre_procedimiento = models.CharField(max_length=61, blank=True, null=True)
    numero_decimales = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caracteristicas'


class CaracteristicasServicio(models.Model):
    codigo_servicio = models.OneToOneField('Servicios', models.DO_NOTHING, db_column='codigo_servicio', primary_key=True)
    codigo_caracteristica = models.ForeignKey(Caracteristicas, models.DO_NOTHING, db_column='codigo_caracteristica')
    rol = models.CharField(max_length=1)
    obligatoria = models.CharField(max_length=1)
    indice = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caracteristicas_servicio'
        unique_together = (('codigo_servicio', 'codigo_caracteristica', 'rol'),)


class CaracteristicasValor(models.Model):
    caracteristica = models.OneToOneField(Caracteristicas, models.DO_NOTHING, db_column='caracteristica', primary_key=True)
    valor = models.DecimalField(max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=255)
    area_aplica = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tipologia = models.CharField(max_length=4, blank=True, null=True)
    accion_ejecutar = models.CharField(max_length=1, blank=True, null=True)
    correo_a = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    duracion = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    unidad_medida = models.CharField(max_length=5, blank=True, null=True)
    valor_padre = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caracteristicas_valor'
        unique_together = (('caracteristica', 'valor'),)


class CiclosAuditoria(models.Model):
    ciclo = models.CharField(primary_key=True, max_length=6)
    estado = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=100)
    fecha_cierre = models.DateTimeField(blank=True, null=True)
    servicio_auditoria = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    servicio_calificar_grupo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    servicio_calificar_auditor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    mensaje_realizar_auditoria = models.CharField(max_length=255, blank=True, null=True)
    mensaje_calificar_auditor = models.CharField(max_length=255, blank=True, null=True)
    mensaje_calificar_grupo = models.CharField(max_length=255, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciclos_auditoria'


class ClientesPreferenciales(models.Model):
    codigo_servicio = models.OneToOneField('Servicios', models.DO_NOTHING, db_column='codigo_servicio', primary_key=True)
    codigo_persona = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=50)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_preferenciales'
        unique_together = (('codigo_servicio', 'codigo_persona'),)


class ContActaInicio(models.Model):
    consecutivo_contrato = models.IntegerField(primary_key=True)
    fecha_acta = models.DateTimeField()
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    anexo_pasadojud = models.CharField(max_length=1, blank=True, null=True)
    anexo_rut = models.CharField(max_length=1, blank=True, null=True)
    anexo_procuraduria = models.CharField(max_length=1, blank=True, null=True)
    anexo_contraloria = models.CharField(max_length=1, blank=True, null=True)
    anexo_contrato = models.CharField(max_length=1, blank=True, null=True)
    anexo_polizas = models.CharField(max_length=1, blank=True, null=True)
    anexo_impuestos = models.CharField(max_length=1, blank=True, null=True)
    anexo_cedula = models.CharField(max_length=1, blank=True, null=True)
    anexo_reg_hab = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_acta_inicio'


class ContAdicionContrato(models.Model):
    consecutivo_adicion = models.IntegerField()
    consecutivo_contrato = models.OneToOneField('ContContrato', models.DO_NOTHING, db_column='consecutivo_contrato', primary_key=True)
    tipo_adicion = models.CharField(max_length=2)
    valor_adicionado = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    plazo_adicionado = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    unidad_plazo = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    clausulas = models.TextField(blank=True, null=True)
    justificacion = models.TextField(blank=True, null=True)
    num_certificacion_add = models.CharField(max_length=25, blank=True, null=True)
    fecha_certificacion_add = models.DateTimeField(blank=True, null=True)
    usuario_insercion = models.CharField(max_length=30, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    valor_adicionado_texto = models.TextField(blank=True, null=True)
    servicio_adicionado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_adicion_contrato'
        unique_together = (('consecutivo_contrato', 'consecutivo_adicion'),)


class ContCdp(models.Model):
    codigo_certificado = models.CharField(primary_key=True, max_length=10)
    valor_certificado = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_expedicion = models.DateTimeField()
    fecha_vencimiento = models.DateTimeField()
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    anio = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'cont_cdp'
        unique_together = (('codigo_certificado', 'anio'),)


class ContCdpContrato(models.Model):
    consecutivo_contrato = models.IntegerField(primary_key=True)
    codigo_certificado = models.ForeignKey(ContCdp, models.DO_NOTHING, db_column='codigo_certificado')
    imputacion = models.CharField(max_length=5000, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    anio = models.CharField(max_length=4)
    consecutivo_adicion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cont_cdp_contrato'
        unique_together = (('consecutivo_contrato', 'consecutivo_adicion', 'codigo_certificado', 'anio'),)


class ContCdpEstudio(models.Model):
    consecutivo_cdp = models.IntegerField()
    anio = models.IntegerField(primary_key=True)
    numero_estudio = models.IntegerField()
    fecha_expedicion = models.DateField()
    codigo_area = models.IntegerField()
    descripcion = models.CharField(max_length=512, blank=True, null=True)
    codigo_imputacion = models.CharField(max_length=15)
    valor_certificado = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    vigencia = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_cdp_estudio'
        unique_together = (('anio', 'consecutivo_cdp'),)


class ContContrato(models.Model):
    consecutivo_contrato = models.AutoField(primary_key=True)
    numero_contrato = models.CharField(max_length=20, blank=True, null=True)
    codigo_sucursal = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_final = models.DateTimeField(blank=True, null=True)
    codigo_rp = models.CharField(max_length=10, blank=True, null=True)
    tipo_doc_interventor = models.CharField(max_length=2, blank=True, null=True)
    doc_interventor = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=2, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    numero_estudio = models.IntegerField(blank=True, null=True)
    fecha_contrato = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fecha_liquidacion = models.DateTimeField(blank=True, null=True)
    valor_liquidacion = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_cancelado = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fecha_anticipo = models.DateTimeField(blank=True, null=True)
    valor_anticipo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    saldo_anticipo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    saldo_contrato = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    condiciones_especiales = models.TextField(blank=True, null=True)
    nro_cc = models.CharField(max_length=16, blank=True, null=True)
    valor_numero = models.FloatField(blank=True, null=True)
    valor_letra = models.CharField(max_length=100, blank=True, null=True)
    plazo_ejecucion = models.CharField(max_length=20, blank=True, null=True)
    cdp_n = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    regimen_tributario = models.CharField(max_length=20, blank=True, null=True)
    supervisor = models.CharField(max_length=20, blank=True, null=True)
    valor_contrato_letra = models.CharField(max_length=150)
    tipo_contrato = models.CharField(max_length=2)
    departamento_contrato = models.CharField(max_length=3, blank=True, null=True)
    municipio_contrato = models.ForeignKey('ParCiudad', models.DO_NOTHING, db_column='municipio_contrato', blank=True, null=True)
    fecha_contrato_hasta = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_contrato'


class ContContratoServicio(models.Model):
    consecutivo_contrato = models.OneToOneField(ContContrato, models.DO_NOTHING, db_column='consecutivo_contrato', primary_key=True)
    codigo_servicio = models.IntegerField()
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_contrato_servicio'
        unique_together = (('consecutivo_contrato', 'codigo_servicio'),)


class ContContratoTarifas(models.Model):
    consecutivo_contrato = models.IntegerField(primary_key=True)
    codigo_procedimiento = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_contrato_tarifas'
        unique_together = (('consecutivo_contrato', 'codigo_procedimiento'),)


class ContEstPrevActividades(models.Model):
    numero_estudio = models.OneToOneField('ContEstudioPrevio', models.DO_NOTHING, db_column='numero_estudio', primary_key=True)
    consecutivo_actividad = models.DecimalField(max_digits=5, decimal_places=0)
    actividad = models.TextField(blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_est_prev_actividades'
        unique_together = (('numero_estudio', 'consecutivo_actividad'),)


class ContEstPrevSubactividades(models.Model):
    numero_estudio = models.OneToOneField('ContEstudioPrevio', models.DO_NOTHING, db_column='numero_estudio', primary_key=True)
    consecutivo_actividad = models.DecimalField(max_digits=5, decimal_places=0)
    consecutivo_subactividad = models.DecimalField(max_digits=5, decimal_places=0)
    subactividad = models.TextField(blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_est_prev_subactividades'
        unique_together = (('numero_estudio', 'consecutivo_actividad', 'consecutivo_subactividad'),)


class ContEstudioPrevio(models.Model):
    numero_estudio = models.IntegerField(primary_key=True)
    tipo_estudio = models.CharField(max_length=1, blank=True, null=True)
    fecha_presentacion = models.DateTimeField()
    objeto_contratar = models.TextField()
    descripcion_necesidad = models.TextField()
    soporte_economico = models.TextField()
    valor = models.FloatField()
    forma_pago = models.CharField(max_length=1)
    forma_pago_descripcion = models.TextField(blank=True, null=True)
    tipo_plazo = models.CharField(max_length=20, blank=True, null=True)
    plazo = models.DecimalField(max_digits=30, decimal_places=20, blank=True, null=True)
    plazo_descripcion = models.TextField(blank=True, null=True)
    tipo_contrato = models.CharField(max_length=2, blank=True, null=True)
    forma_contrato = models.CharField(max_length=1, blank=True, null=True)
    tarifa = models.CharField(max_length=1, blank=True, null=True)
    tarifa_descripcion = models.TextField(blank=True, null=True)
    lugar_ejecucion = models.TextField()
    clase_gasto = models.CharField(max_length=2)
    aplica_iva = models.CharField(max_length=1, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    valor_texto = models.TextField(blank=True, null=True)
    dependencia = models.IntegerField(blank=True, null=True)
    porcentaje_anticipo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    porcentaje_tarifa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    interventor = models.CharField(max_length=100, blank=True, null=True)
    justificacion_valor = models.TextField(blank=True, null=True)
    empleado_supervisor = models.IntegerField(blank=True, null=True)
    actividad_especifica = models.CharField(max_length=3, blank=True, null=True)
    fecha_desde = models.DateField(blank=True, null=True)
    fecha_hasta = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_estudio_previo'


class ContEstudioPrevioFirma(models.Model):
    numero_estudio = models.OneToOneField(ContEstudioPrevio, models.DO_NOTHING, db_column='numero_estudio', primary_key=True)
    tipo_firma = models.CharField(max_length=2)
    funcionario = models.IntegerField()
    descripcion_firma = models.TextField()
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=10, blank=True, null=True) #para_eliminar tenia -1 en max_length

    class Meta:
        managed = False
        db_table = 'cont_estudio_previo_firma'
        unique_together = (('numero_estudio', 'tipo_firma'),)


class ContEstudioPrevioItems(models.Model):
    numero_estudio = models.OneToOneField(ContEstudioPrevio, models.DO_NOTHING, db_column='numero_estudio', primary_key=True)
    consecutivo_item = models.DecimalField(max_digits=3, decimal_places=0)
    tipo_item = models.CharField(max_length=30)
    descripcion_item = models.TextField()
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=10, blank=True, null=True) #para_eliminar tenia -1 en max_length

    class Meta:
        managed = False
        db_table = 'cont_estudio_previo_items'
        unique_together = (('numero_estudio', 'consecutivo_item'),)


class ContEstudioPrevioServicios(models.Model):
    numero_estudio = models.OneToOneField(ContEstudioPrevio, models.DO_NOTHING, db_column='numero_estudio', primary_key=True)
    codigo_servicio = models.IntegerField()
    departamento = models.CharField(max_length=2)
    ciudad = models.CharField(max_length=3)
    imputacion = models.CharField(max_length=200, blank=True, null=True)
    valor_upc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    afiliados = models.IntegerField(blank=True, null=True)
    meses = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    dias = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    valor_mes = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    porcentaje_afiliados = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_estudio_previo_servicios'
        unique_together = (('numero_estudio', 'codigo_servicio', 'departamento', 'ciudad'),)


class ContEstudioPrevioTarifas(models.Model):
    numero_estudio = models.OneToOneField(ContEstudioPrevio, models.DO_NOTHING, db_column='numero_estudio', primary_key=True)
    tipo_cuadro = models.CharField(max_length=2)
    consecutivo = models.DecimalField(max_digits=15, decimal_places=0)
    valor_1 = models.CharField(max_length=2000, blank=True, null=True)
    valor_2 = models.CharField(max_length=2000, blank=True, null=True)
    valor_3 = models.CharField(max_length=2000, blank=True, null=True)
    valor_4 = models.CharField(max_length=2000, blank=True, null=True)
    valor_5 = models.CharField(max_length=2000, blank=True, null=True)
    valor_6 = models.CharField(max_length=2000, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=5, blank=True, null=True)
    titulo = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'cont_estudio_previo_tarifas'
        unique_together = (('numero_estudio', 'tipo_cuadro', 'titulo', 'consecutivo'),)


class ContImpuesto(models.Model):
    consecutivo_contrato = models.ForeignKey(ContContrato, models.DO_NOTHING, db_column='consecutivo_contrato')
    numero_recibo = models.CharField(primary_key=True, max_length=25)
    fecha_pago = models.DateTimeField()
    valor_pago = models.DecimalField(max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_impuesto'
        unique_together = (('numero_recibo', 'descripcion', 'consecutivo_contrato'),)


class ContImputacionPresupuestal(models.Model):
    codigo_imputacion = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=50)
    anio = models.IntegerField()
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=10, blank=True, null=True) #para_eliminar tenia -1 en max_length

    class Meta:
        managed = False
        db_table = 'cont_imputacion_presupuestal'
        unique_together = (('codigo_imputacion', 'anio'),)


class ContInterventor(models.Model):
    tipo_documento = models.CharField(primary_key=True, max_length=2)
    numero_documento = models.DecimalField(max_digits=10, decimal_places=0)
    apellidos = models.CharField(max_length=60, blank=True, null=True)
    nombres = models.CharField(max_length=60, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_interventor'
        unique_together = (('tipo_documento', 'numero_documento'),)


class ContPoliza(models.Model):
    consecutivo_contrato = models.OneToOneField(ContContrato, models.DO_NOTHING, db_column='consecutivo_contrato', primary_key=True)
    numero_poliza = models.CharField(max_length=40)
    tipo_poliza = models.CharField(max_length=25)
    entidad_expide = models.CharField(max_length=40)
    fecha_expedicion = models.DateTimeField()
    fecha_aprobacion = models.DateTimeField()
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_final = models.DateTimeField(blank=True, null=True)
    valor = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_poliza'
        unique_together = (('consecutivo_contrato', 'numero_poliza', 'tipo_poliza'),)


class ContRp(models.Model):
    numero_registro = models.CharField(primary_key=True, max_length=25)
    fecha_expedicion = models.DateTimeField(blank=True, null=True)
    valor = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    dependencia = models.IntegerField(blank=True, null=True)
    consecutivo_contrato = models.IntegerField()
    numero_adicion = models.IntegerField()
    anio = models.CharField(max_length=4)
    imputacion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_rp'
        unique_together = (('numero_registro', 'anio'),)


class DatosAuditoria(models.Model):
    codigo_empleado = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    ciclo = models.CharField(max_length=6)
    participo = models.CharField(max_length=1, blank=True, null=True)
    evaluacion_auditado = models.CharField(max_length=1, blank=True, null=True)
    evaluacion_gestion = models.CharField(max_length=1, blank=True, null=True)
    tipo_auditoria = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    clase_auditoria = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    ntipo_auditoria = models.CharField(max_length=50, blank=True, null=True)
    nclase_auditoria = models.CharField(max_length=50, blank=True, null=True)
    veces = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datos_auditoria'
        unique_together = (('codigo_empleado', 'ciclo'),)


class DetalleAuditoria(models.Model):
    codigo_empleado = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    ciclo = models.CharField(max_length=6)
    consecutivo = models.DecimalField(max_digits=10, decimal_places=0)
    rol = models.CharField(max_length=1, blank=True, null=True)
    area_auditada = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    persona_auditada = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    asistio = models.CharField(max_length=1, blank=True, null=True)
    generado = models.CharField(max_length=1, blank=True, null=True)
    solicitud = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_auditoria'
        unique_together = (('codigo_empleado', 'ciclo', 'consecutivo'),)


class DetalleEncuesta(models.Model):
    numero = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    caracteristica = models.DecimalField(max_digits=10, decimal_places=0)
    consecutivo = models.DecimalField(max_digits=10, decimal_places=0)
    observacion = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_encuesta'
        unique_together = (('numero', 'caracteristica', 'consecutivo'),)


class DetallesSolicitud(models.Model):
    numero_solicitud = models.OneToOneField('Solicitudes', models.DO_NOTHING, db_column='numero_solicitud', primary_key=True)
    consecutivo_detalle = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_caracteristica = models.ForeignKey(Caracteristicas, models.DO_NOTHING, db_column='codigo_caracteristica')
    fecha_diligenciamiento = models.DateTimeField()
    observacion = models.CharField(max_length=4000, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalles_solicitud'
        unique_together = (('numero_solicitud', 'consecutivo_detalle', 'codigo_caracteristica'),)


class DiasFestivos(models.Model):
    fecha = models.DateField(primary_key=True)
    nombre = models.CharField(max_length=50)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dias_festivos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Encuesta(models.Model):
    numero = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    empleado_cliente = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    codigo_servicio = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.DecimalField(max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    codigo_confiabilidad = models.CharField(max_length=1, blank=True, null=True)
    justificacion = models.CharField(max_length=100, blank=True, null=True)
    ciclo = models.CharField(max_length=6, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    area_cliente = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'encuesta'


class Encuestados(models.Model):
    numero = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    proveedor = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    area_proveedor = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'encuestados'
        unique_together = (('numero', 'proveedor', 'area_proveedor'),)


class EscalamientosAreaServicio(models.Model):
    anno = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    mes = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_area = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_servicio = models.DecimalField(max_digits=10, decimal_places=0)
    solicitudes_recibidas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    solicitudes_atendidas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    solicitudes_escaladas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    acciones_mejora = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escalamientos_area_servicio'
        unique_together = (('anno', 'mes', 'codigo_area', 'codigo_servicio'),)


class EstadoEncuesta(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=30)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_encuesta'


class Estados(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=40)
    tipo_estado = models.CharField(max_length=3)
    califica = models.CharField(max_length=1)
    confiabilidad = models.CharField(max_length=1)
    oportunidad = models.CharField(max_length=1)
    cierra = models.CharField(max_length=1)
    rol_genera_mail = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    porcentaje_aparece = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados'


class EstadosDependencia(models.Model):
    codigo = models.CharField(primary_key=True, max_length=1)
    descripcion = models.CharField(max_length=40)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados_dependencia'


class EstadosDetalle(models.Model):
    codigo = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=40)
    rol_aplica = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados_detalle'


class EstadosPersonas(models.Model):
    codigo = models.CharField(primary_key=True, max_length=1)
    descripcion = models.CharField(max_length=40)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados_personas'


class Fabian(models.Model):
    codigo_fabian = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    nombre_fabian = models.CharField(max_length=50, blank=True, null=True)
    apellidos_fabian = models.CharField(max_length=50, blank=True, null=True)
    direccion_fabian = models.CharField(max_length=10, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fabian'


class Formula(models.Model):
    id_formula = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    formula = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=500)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formula'


class HistoriaSolicitud(models.Model):
    numero_solicitud = models.OneToOneField('Solicitudes', models.DO_NOTHING, db_column='numero_solicitud', primary_key=True)
    consecutivo_historia = models.DecimalField(max_digits=10, decimal_places=0)
    estado_final = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_cambio = models.DateTimeField()
    estado_inicial = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historia_solicitud'
        unique_together = (('numero_solicitud', 'consecutivo_historia'),)


class IndicadorActividades(models.Model):
    id_indicador = models.CharField(primary_key=True, max_length=10)
    mes = models.CharField(max_length=100)
    porcentaje = models.DecimalField(max_digits=15, decimal_places=0)
    ciclo = models.DecimalField(max_digits=4, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    retrasos_soluciones = models.CharField(max_length=1000, blank=True, null=True)
    avances = models.CharField(max_length=1000, blank=True, null=True)
    logros_beneficios = models.CharField(max_length=1000, blank=True, null=True)
    comentarios_adicionales = models.CharField(max_length=1000, blank=True, null=True)
    accion_tomada = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicador_actividades'
        unique_together = (('id_indicador', 'mes'),)


class IndicadorCaracteristica(models.Model):
    id_registro = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    ciclo = models.DecimalField(max_digits=4, decimal_places=0)
    indicador = models.CharField(max_length=10)
    mes = models.CharField(max_length=10)
    caracteristica = models.DecimalField(max_digits=10, decimal_places=0)
    valor_programado = models.DecimalField(max_digits=15, decimal_places=0)
    valor_ejecutado = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicador_caracteristica'


class IndicadorResultados(models.Model):
    ciclo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    indicador = models.CharField(max_length=10)
    mes = models.CharField(max_length=10)
    valor_programado = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    valor_ejecutado = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    estado = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'indicador_resultados'
        unique_together = (('ciclo', 'indicador', 'mes'),)


class IndicadorVariables(models.Model):
    indicador = models.CharField(primary_key=True, max_length=10)
    variable = models.DecimalField(max_digits=4, decimal_places=0)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fuente_informacion = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicador_variables'
        unique_together = (('indicador', 'variable'),)


class Indicadores(models.Model):
    codigo_indicador = models.CharField(primary_key=True, max_length=10)
    proceso = models.DecimalField(max_digits=4, decimal_places=0)
    area = models.DecimalField(max_digits=10, decimal_places=0)
    ciclo = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    objetivo_estrategico = models.DecimalField(max_digits=3, decimal_places=0)
    indicador_acuerdo = models.CharField(max_length=255, blank=True, null=True)
    tipo_indicador = models.CharField(max_length=10)
    proyecto_inversion = models.CharField(max_length=10, blank=True, null=True)
    meta_plan_de_desarrollo = models.DecimalField(max_digits=3, decimal_places=0)
    meta_proyecto = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    nombre_indicador = models.CharField(max_length=100)
    objetivo_indicador = models.CharField(max_length=200)
    prioridad_en_producto = models.CharField(max_length=50)
    formula = models.CharField(max_length=50, blank=True, null=True)
    unidad_medida = models.IntegerField(blank=True, null=True)
    frecuencia_medicion = models.CharField(max_length=7, blank=True, null=True)
    producto_pmr = models.CharField(max_length=2, blank=True, null=True)
    mes1 = models.CharField(max_length=10, blank=True, null=True)
    mes2 = models.CharField(max_length=10, blank=True, null=True)
    mes3 = models.CharField(max_length=10, blank=True, null=True)
    mes4 = models.CharField(max_length=10, blank=True, null=True)
    mes5 = models.CharField(max_length=10, blank=True, null=True)
    mes6 = models.CharField(max_length=10, blank=True, null=True)
    mes7 = models.CharField(max_length=10, blank=True, null=True)
    mes8 = models.CharField(max_length=10, blank=True, null=True)
    mes9 = models.CharField(max_length=10, blank=True, null=True)
    mes10 = models.CharField(max_length=10, blank=True, null=True)
    mes11 = models.CharField(max_length=10, blank=True, null=True)
    mes12 = models.CharField(max_length=10, blank=True, null=True)
    valormes1 = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    valormes2 = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    valormes3 = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    valormes4 = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    valormes5 = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    valormes6 = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    valormes7 = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    valormes8 = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    valormes9 = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    valormes10 = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    valormes11 = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    valormes12 = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    meta_total_programada = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    acumulado_vigencias = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    acumulado_esta_vigencia = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    logro_total = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    logro_acumulado_total = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    meta_esta_vigencia = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicadores'


class Labores(models.Model):
    solicitud = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    consecutivo = models.DecimalField(max_digits=10, decimal_places=0)
    tipo_labor = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=1, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    fecha_aplica = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labores'
        unique_together = (('solicitud', 'consecutivo'),)


class MacroServicios(models.Model):
    codigo_servicio = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    codigo_anidado = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    valor_caracteristica = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'macro_servicios'
        unique_together = (('codigo_servicio', 'codigo_anidado'),)


class Mensajes(models.Model):
    codigo = models.CharField(primary_key=True, max_length=40)
    descripcion = models.CharField(max_length=255)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensajes'


class MisionArea(models.Model):
    area = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    mision1 = models.CharField(max_length=255, blank=True, null=True)
    mision2 = models.CharField(max_length=255, blank=True, null=True)
    mision3 = models.CharField(max_length=255, blank=True, null=True)
    mision4 = models.CharField(max_length=255, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mision_area'


class ParCiudad(models.Model):
    codigo_ciudad = models.CharField(primary_key=True, max_length=3)
    nombre_ciudad = models.CharField(max_length=100, blank=True, null=True)
    codigo_departamento = models.ForeignKey('ParDepartamento', models.DO_NOTHING, db_column='codigo_departamento')
    incremento_soat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'par_ciudad'
        unique_together = (('codigo_ciudad', 'codigo_departamento'),)


class ParDepartamento(models.Model):
    codigo_departamento = models.CharField(primary_key=True, max_length=2)
    nombre_departamento = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'par_departamento'


class ParametrosAplicacion(models.Model):
    codigo = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    entero = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    real = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    caracter = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    control = models.CharField(max_length=2, blank=True, null=True)
    batch = models.CharField(max_length=1, blank=True, null=True)
    linea = models.CharField(max_length=1, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametros_aplicacion'


class PdeAnios(models.Model):
    id_anio = models.IntegerField(primary_key=True)
    id_meta = models.ForeignKey('PdeMetas', models.DO_NOTHING, db_column='id_meta')
    anio = models.IntegerField()
    programado = models.CharField(max_length=20, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=100)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)
    ejecutado = models.CharField(max_length=20, blank=True, null=True)
    tr1_programado = models.CharField(max_length=20, blank=True, null=True)
    tr1_ejecutado = models.CharField(max_length=20, blank=True, null=True)
    tr2_programado = models.CharField(max_length=20, blank=True, null=True)
    tr2_ejecutado = models.CharField(max_length=20, blank=True, null=True)
    tr3_programado = models.CharField(max_length=20, blank=True, null=True)
    tr3_ejecutado = models.CharField(max_length=20, blank=True, null=True)
    tr4_programado = models.CharField(max_length=20, blank=True, null=True)
    tr4_ejecutado = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pde_anios'


class PdeMetas(models.Model):
    id_meta = models.IntegerField(primary_key=True)
    codigo_meta = models.CharField(max_length=10)
    id_unidad_nivel = models.ForeignKey('PdeUnidadNivel', models.DO_NOTHING, db_column='id_unidad_nivel', blank=True, null=True)
    id_objetivo_especifico = models.ForeignKey('PdeObjetivosEspecificos', models.DO_NOTHING, db_column='id_objetivo_especifico', blank=True, null=True)
    codigo_unidad = models.CharField(max_length=5)
    nombre_meta = models.CharField(max_length=200)
    cantidad = models.CharField(max_length=20)
    linea_base = models.CharField(max_length=20)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=100)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)
    indicador = models.CharField(max_length=200, blank=True, null=True)
    tipo_meta = models.CharField(max_length=1, blank=True, null=True)
    proceso = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pde_metas'

    def __str__(self):
        return u'%s' % (self.nombre_meta)


class PdeMetasResponsables(models.Model):
    id_meta = models.IntegerField(primary_key=True)
    codigo_cargo = models.CharField(max_length=5)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pde_metas_responsables'
        unique_together = (('id_meta', 'codigo_cargo'),)


class PdeNivelPlan(models.Model):
    id_nivel = models.IntegerField(primary_key=True)
    id_plan_desarrollo = models.ForeignKey('PdePlanDesarrollo', models.DO_NOTHING, db_column='id_plan_desarrollo')
    nivel_superior = models.ForeignKey('self', models.DO_NOTHING, db_column='nivel_superior', blank=True, null=True)
    nombre_nivel = models.CharField(max_length=50)
    tipo_nivel = models.SmallIntegerField()
    objetivo_general = models.CharField(max_length=1, blank=True, null=True)
    objetivo_especifico = models.CharField(max_length=1, blank=True, null=True)
    metas_general = models.CharField(max_length=1, blank=True, null=True)
    metas_especifico = models.CharField(max_length=1, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=100)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pde_nivel_plan'


class PdeObjetivosEspecificos(models.Model):
    id_objetivo_especifico = models.IntegerField(primary_key=True)
    codigo_objetivo_especifico = models.CharField(max_length=10)
    id_unidad_nivel = models.ForeignKey('PdeUnidadNivel', models.DO_NOTHING, db_column='id_unidad_nivel')
    descripcion_objetivo_especifico = models.CharField(max_length=255)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=100)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pde_objetivos_especificos'


class PdePlanDesarrollo(models.Model):
    id_plan_desarrollo = models.SmallIntegerField(primary_key=True)
    nit_entidad = models.ForeignKey('SisEntidad', models.DO_NOTHING, db_column='nit_entidad')
    nombre_plan_desarrollo = models.CharField(max_length=50)
    aprobacion = models.CharField(max_length=15, blank=True, null=True)
    nro_aprobacion = models.IntegerField(blank=True, null=True)
    fecha_aprobacion = models.DateField(blank=True, null=True)
    fecha_inicial = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=100)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)
    cargado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pde_plan_desarrollo'


class PdeUnidadNivel(models.Model):
    id_unidad_nivel = models.IntegerField(primary_key=True)
    codigo_unidad = models.CharField(max_length=10)
    id_nivel = models.ForeignKey(PdeNivelPlan, models.DO_NOTHING, db_column='id_nivel')
    id_unidad_superior = models.ForeignKey('self', models.DO_NOTHING, db_column='id_unidad_superior', blank=True, null=True)
    nombre_unidad = models.CharField(max_length=100, blank=True, null=True)
    objetivo_general = models.CharField(max_length=255, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=100)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pde_unidad_nivel'

    def __str__(self):
        return u'%s %s' % (self.codigo_unidad, self.nombre_unidad)


class PoaActividadResponsable(models.Model):
    id_actividad = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    id_usuario = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_poa = models.DecimalField(max_digits=4, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_actividad_responsable'
        unique_together = (('id_actividad', 'id_usuario', 'codigo_poa'),)


class PoaActividades(models.Model):
    codigo_actividad = models.DecimalField(primary_key=True, max_digits=3, decimal_places=0)
    descripcion = models.CharField(max_length=400, blank=True, null=True)
    tipo_actividad = models.CharField(max_length=2)
    area = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_actividades'


class PoaCiclos(models.Model):
    codigo_ciclo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_ciclos'


class PoaColoresSemaforo(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    tipo_semaforo = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    valor_inicial = models.DecimalField(max_digits=5, decimal_places=0)
    valor_final = models.DecimalField(max_digits=5, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_colores_semaforo'


class PoaInsumos(models.Model):
    codigo_insumo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    descrpcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_insumos'


class PoaLogros(models.Model):
    id_logro = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    codigo_poa = models.DecimalField(max_digits=4, decimal_places=0)
    mes = models.CharField(max_length=100, blank=True, null=True)
    ejecucion = models.DecimalField(max_digits=10, decimal_places=0)
    avances = models.CharField(max_length=1000, blank=True, null=True)
    logros_y_resultados = models.CharField(max_length=1000, blank=True, null=True)
    retrasos_dificultades = models.CharField(max_length=1000, blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_logros'


class PoaMaestro(models.Model):
    codigo_poa = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    proceso = models.DecimalField(max_digits=4, decimal_places=0)
    area = models.DecimalField(max_digits=10, decimal_places=0)
    responsable = models.DecimalField(max_digits=10, decimal_places=0)
    ciclo = models.DecimalField(max_digits=4, decimal_places=0)
    estado = models.CharField(max_length=1, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_maestro'
        unique_together = (('ciclo', 'area', 'proceso'),)


class PoaMaestroActividades(models.Model):
    codigo_poa = models.DecimalField(max_digits=4, decimal_places=0)
    codigo_poa_actividad = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    objetivo_estrategico = models.DecimalField(max_digits=3, decimal_places=0)
    actividad = models.DecimalField(max_digits=3, decimal_places=0)
    tipo_actividad = models.DecimalField(max_digits=3, decimal_places=0)
    variables_medicion = models.CharField(max_length=10)
    proyecto_inversion = models.CharField(max_length=10)
    producto_proceso = models.DecimalField(max_digits=3, decimal_places=0)
    meta_plan_de_desarrollo = models.DecimalField(max_digits=3, decimal_places=0)
    objetivo_subsistema = models.DecimalField(max_digits=3, decimal_places=0)
    meta_proyecto = models.DecimalField(max_digits=3, decimal_places=0)
    tipo_recurso = models.CharField(max_length=50)
    prioridad_en_producto = models.CharField(max_length=50)
    prioridad_objetivo = models.CharField(max_length=50)
    mes1 = models.CharField(max_length=7, blank=True, null=True)
    mes2 = models.CharField(max_length=7, blank=True, null=True)
    mes3 = models.CharField(max_length=7, blank=True, null=True)
    mes4 = models.CharField(max_length=7, blank=True, null=True)
    mes5 = models.CharField(max_length=7, blank=True, null=True)
    mes6 = models.CharField(max_length=7, blank=True, null=True)
    mes7 = models.CharField(max_length=7, blank=True, null=True)
    mes8 = models.CharField(max_length=7, blank=True, null=True)
    mes9 = models.CharField(max_length=7, blank=True, null=True)
    mes10 = models.CharField(max_length=7, blank=True, null=True)
    mes11 = models.CharField(max_length=7, blank=True, null=True)
    mes12 = models.CharField(max_length=7, blank=True, null=True)
    valor_mes1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_mes2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_mes3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_mes4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_mes5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_mes6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_mes7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_mes8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_mes9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_mes10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_mes11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_mes12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_maestro_actividades'


class PoaMaestroDetalle(models.Model):
    id_detalle = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    codigo_poa = models.DecimalField(max_digits=4, decimal_places=0)
    valor_mes1 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    valor_mes2 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    valor_mes3 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    valor_mes4 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    valor_mes5 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    valor_mes6 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    valor_mes7 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    valor_mes8 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    valor_mes9 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    valor_mes10 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    valor_mes11 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    valor_mes12 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_maestro_detalle'


class PoaMaestroInsumo(models.Model):
    insumo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    maestro = models.DecimalField(max_digits=4, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_maestro_insumo'
        unique_together = (('insumo', 'maestro'),)


class PoaMaestroInsumoProveedor(models.Model):
    id_insumo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    id_proveedor = models.DecimalField(max_digits=10, decimal_places=0)
    id_maestro = models.DecimalField(max_digits=4, decimal_places=0)
    fecha_programada_entrega = models.DateTimeField()
    fecha_real_entrega = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_maestro_insumo_proveedor'
        unique_together = (('id_insumo', 'id_maestro', 'id_proveedor'),)


class PoaMaestroMedioVerif(models.Model):
    id_maestro = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    id_medio_verificacion = models.DecimalField(max_digits=3, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    codigo_poa_actividad = models.DecimalField(max_digits=4, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'poa_maestro_medio_verif'
        unique_together = (('id_maestro', 'codigo_poa_actividad', 'id_medio_verificacion'),)


class PoaMaestroMultivalores(models.Model):
    codigo_poa = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    tabla = models.CharField(max_length=100)
    valor = models.CharField(max_length=1)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    codigo_poa_actividad = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_maestro_multivalores'
        unique_together = (('codigo_poa', 'tabla', 'valor'),)


class PoaMaestroProveedor(models.Model):
    maestro = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    proveedor = models.DecimalField(max_digits=3, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_maestro_proveedor'
        unique_together = (('maestro', 'proveedor'),)


class PoaMaestroResponsable(models.Model):
    codigo_maestro = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    codigo_empleado = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_maestro_responsable'
        unique_together = (('codigo_maestro', 'codigo_empleado'),)


class PoaMediosVerificacion(models.Model):
    codigo_medio_verificacion = models.DecimalField(primary_key=True, max_digits=3, decimal_places=0)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_medios_verificacion'


class PoaMetasPlanDesarrollo(models.Model):
    codigo_meta_plan = models.DecimalField(primary_key=True, max_digits=3, decimal_places=0)
    descripcion = models.CharField(max_length=400)
    area = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    codigo_proyecto_inversion = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_metas_plan_desarrollo'


class PoaMetasProyecto(models.Model):
    codigo_meta_proyecto = models.DecimalField(primary_key=True, max_digits=3, decimal_places=0)
    descripcion = models.CharField(max_length=400)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    codigo_proyecto_inversion = models.CharField(max_length=10, blank=True, null=True)
    meta_plan = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_metas_proyecto'


class PoaObjetivosEstrategicos(models.Model):
    codigo_objetivo = models.DecimalField(primary_key=True, max_digits=3, decimal_places=0)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_objetivos_estrategicos'


class PoaObjetivosSubsistemaSig(models.Model):
    codigo_objetivo_subsistema = models.DecimalField(primary_key=True, max_digits=3, decimal_places=0)
    descripcion = models.CharField(max_length=110)
    area = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_objetivos_subsistema_sig'


class PoaProcesos(models.Model):
    codigo_proceso = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    tipo_proceso = models.CharField(max_length=1, blank=True, null=True)
    lider_proceso = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_procesos'


class PoaProductosProceso(models.Model):
    codigo_producto_proceso = models.DecimalField(primary_key=True, max_digits=3, decimal_places=0)
    descripcion = models.CharField(max_length=400)
    area = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_productos_proceso'


class PoaProveedores(models.Model):
    codigo_proveedor = models.DecimalField(primary_key=True, max_digits=3, decimal_places=0)
    descripcion = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_proveedores'


class PoaProyectosInversion(models.Model):
    codigo_proyecto_inversion = models.CharField(primary_key=True, max_length=13)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    objetivo_proyecto = models.CharField(max_length=255, blank=True, null=True)
    valor_proyecto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fecha_radicado = models.DateField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_terminacion = models.DateField(blank=True, null=True)
    fase = models.CharField(max_length=100, blank=True, null=True)
    ejecutor = models.CharField(max_length=100, blank=True, null=True)
    fuente = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_proyectos_inversion'


class PoaTableroColores(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    color = models.CharField(max_length=100)
    valor_inicial = models.DecimalField(max_digits=5, decimal_places=0)
    valor_final = models.DecimalField(max_digits=5, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa_tablero_colores'


class Procesos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=20)
    descripcion = models.CharField(max_length=120)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    tipo_proceso = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procesos'

    def __str__(self):
        return u'%s' % (self.descripcion)


class ProcesosServicios(models.Model):
    proceso = models.CharField(primary_key=True, max_length=20)
    subproceso = models.CharField(max_length=20)
    servicio = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=120)
    estado = models.CharField(max_length=1, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procesos_servicios'
        unique_together = (('proceso', 'subproceso', 'servicio'),)


class ProveedorMultiple(models.Model):
    codigo_area = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    codigo_servicio = models.DecimalField(max_digits=10, decimal_places=0)
    persona_cargo = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    fecha_asignacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor_multiple'
        unique_together = (('codigo_area', 'codigo_servicio', 'persona_cargo'),)


class ProveedoresExternos(models.Model):
    codigo_proveedor = models.CharField(primary_key=True, max_length=30)
    nit_proveedor = models.CharField(max_length=15, blank=True, null=True)
    nombre_proveedor = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    telefonos = models.CharField(max_length=60, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    correo_electronico = models.CharField(max_length=60, blank=True, null=True)
    actividad_principal = models.CharField(max_length=60, blank=True, null=True)
    numero_funcionarios = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=30)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores_externos'


class RedPrestador(models.Model):
    numero_identificacion = models.CharField(primary_key=True, max_length=16)
    tipo_identificacion = models.CharField(max_length=3)
    dv = models.IntegerField(blank=True, null=True)
    codigo_habilitacion = models.CharField(max_length=12, blank=True, null=True)
    nombre_entidad = models.CharField(max_length=200)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    tipo_documento_representate = models.CharField(max_length=3, blank=True, null=True)
    documento_representante = models.CharField(max_length=16, blank=True, null=True)
    complejidad = models.CharField(max_length=1, blank=True, null=True)
    resolucion_creacion = models.CharField(max_length=20, blank=True, null=True)
    primer_nombre_representante = models.CharField(max_length=30, blank=True, null=True)
    segundo_nombre_representante = models.CharField(max_length=30, blank=True, null=True)
    primer_apellido_representante = models.CharField(max_length=30, blank=True, null=True)
    segundo_apellido_representante = models.CharField(max_length=30, blank=True, null=True)
    clase_prestador = models.CharField(max_length=2, blank=True, null=True)
    tipo_persona = models.CharField(max_length=2, blank=True, null=True)
    naturaleza_juridica = models.CharField(max_length=2, blank=True, null=True)
    sitio_web = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    forma_vinculacion_representante = models.CharField(max_length=30, blank=True, null=True)
    caracter_territorial = models.CharField(max_length=2, blank=True, null=True)
    empresa_social_estado = models.CharField(max_length=2, blank=True, null=True)
    acto_constitucion = models.CharField(max_length=2, blank=True, null=True)
    numero_acto = models.CharField(max_length=30, blank=True, null=True)
    fecha_acto = models.DateTimeField(blank=True, null=True)
    entidad_expide = models.CharField(max_length=30, blank=True, null=True)
    departamento = models.CharField(max_length=2, blank=True, null=True)
    municipio = models.CharField(max_length=3, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    departamento_representante = models.CharField(max_length=3, blank=True, null=True)
    municipio_representante = models.CharField(max_length=3, blank=True, null=True)
    departamento_expedicion = models.CharField(max_length=3, blank=True, null=True)
    municipio_expedicion = models.CharField(max_length=3, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    nivel_atencion = models.CharField(max_length=2, blank=True, null=True)
    tipo_prestador = models.CharField(max_length=10, blank=True, null=True)
    numero_registro = models.CharField(max_length=50)
    numero_libro = models.CharField(max_length=50)
    numero_folio = models.CharField(max_length=50)
    fecha_inscripcion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'red_prestador'


class RedPrestadorDocumentos(models.Model):
    numero_identificacion = models.OneToOneField(RedPrestador, models.DO_NOTHING, db_column='numero_identificacion', primary_key=True)
    tipo_documento = models.CharField(max_length=50)
    codigo_sucursal = models.IntegerField()
    tiene_imagen = models.CharField(max_length=1, blank=True, null=True)
    fecha_emision = models.DateTimeField(blank=True, null=True)
    fecha_caducidad = models.DateTimeField(blank=True, null=True)
    valor_documento = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'red_prestador_documentos'
        unique_together = (('numero_identificacion', 'tipo_documento', 'codigo_sucursal'),)


class RedSucursal(models.Model):
    codigo_sucursal = models.IntegerField(primary_key=True)
    numero_identificacion = models.ForeignKey(RedPrestador, models.DO_NOTHING, db_column='numero_identificacion')
    codigo_habilitacion = models.CharField(max_length=12, blank=True, null=True)
    numero_sede = models.IntegerField(blank=True, null=True)
    nombre_sede = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=2, blank=True, null=True)
    municipio = models.CharField(max_length=3, blank=True, null=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    estado = models.CharField(max_length=2, blank=True, null=True)
    sede_principal = models.CharField(max_length=2, blank=True, null=True)
    zona = models.CharField(max_length=2, blank=True, null=True)
    barrio = models.CharField(max_length=70, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    primer_nombre_director = models.CharField(max_length=30, blank=True, null=True)
    segundo_nombre_director = models.CharField(max_length=30, blank=True, null=True)
    primer_apellido_director = models.CharField(max_length=30, blank=True, null=True)
    segundo_apellido_director = models.CharField(max_length=30, blank=True, null=True)
    tipo_identificacion_director = models.CharField(max_length=2, blank=True, null=True)
    numero_identificacion_director = models.CharField(max_length=16, blank=True, null=True)
    centro_poblado = models.CharField(max_length=100, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    facturacion_agrupada = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'red_sucursal'


class Refuerzos(models.Model):
    area = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    tipo = models.CharField(max_length=1)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refuerzos'


class ReportesCliente(models.Model):
    numero = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=4000, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_insercion = models.CharField(max_length=50, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reportes_cliente'


class Roles(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=40)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class SecuenciaEstados(models.Model):
    codigo_estado_inicial = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    codigo_estado_final = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_rol = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secuencia_estados'
        unique_together = (('codigo_estado_inicial', 'codigo_estado_final'),)


class ServicioTareas(models.Model):
    codigo_servicio = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    consecutivo_tarea = models.DecimalField(max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=100)
    duracion = models.DecimalField(max_digits=10, decimal_places=0)
    unidad_medida = models.CharField(max_length=2)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio_tareas'
        unique_together = (('codigo_servicio', 'consecutivo_tarea'),)


class Servicios(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=100)
    especializado = models.CharField(max_length=1)
    duracion = models.DecimalField(max_digits=10, decimal_places=0)
    unidad_medida = models.CharField(max_length=5)
    porcentaje_esc_1 = models.DecimalField(max_digits=10, decimal_places=0)
    porcentaje_esc_2 = models.DecimalField(max_digits=10, decimal_places=0)
    porcentaje_esc_3 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    porcentaje_esc_4 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    porcentaje_esc_5 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    porcentaje_esc_6 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    anidar = models.CharField(max_length=1, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    tipo_servicio = models.CharField(max_length=2, blank=True, null=True)
    cambia_proveedor = models.CharField(max_length=1, blank=True, null=True)
    permite_devolver = models.CharField(max_length=1, blank=True, null=True)
    reasignar_auditor = models.CharField(max_length=1, blank=True, null=True)
    calificar_servicio = models.CharField(max_length=1, blank=True, null=True)
    area_padre = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cliente_preferencia = models.CharField(max_length=1, blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    mensaje = models.CharField(max_length=1000, blank=True, null=True)
    archivo_anexo = models.CharField(max_length=80, blank=True, null=True)
    permite_devolver_politicas = models.CharField(max_length=1, blank=True, null=True)
    autonumerar_solicitud = models.CharField(max_length=1, blank=True, null=True)
    permite_devolver_atencion = models.CharField(max_length=1, blank=True, null=True)
    calcular_prontitud = models.CharField(max_length=1, blank=True, null=True)
    permitir_escoger_proveedor = models.CharField(max_length=1, blank=True, null=True)
    numero_anexos = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    autoaceptar_aplamientos = models.CharField(max_length=1, blank=True, null=True)
    cerrar_por_escalamientos = models.CharField(max_length=1, blank=True, null=True)
    ind_flujo_trabajo = models.CharField(max_length=1, blank=True, null=True)
    ind_nomina = models.CharField(max_length=1, blank=True, null=True)
    numero_anexos_envio = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ind_correo_calificacion = models.CharField(max_length=1, blank=True, null=True)
    ind_avanzar_caracteristica = models.CharField(max_length=1, blank=True, null=True)
    correo_notificacion = models.CharField(max_length=50, blank=True, null=True)
    escalar_a = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    proceso = models.CharField(max_length=20, blank=True, null=True)
    subproceso = models.CharField(max_length=20, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios'


class ServiciosAnidados(models.Model):
    codigo_servicio = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    codigo_anidado = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=30, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios_anidados'
        unique_together = (('codigo_servicio', 'codigo_anidado'),)


class ServiciosArea(models.Model):
    codigo_area = models.OneToOneField('UnidadesDependencia', models.DO_NOTHING, db_column='codigo_area', primary_key=True)
    codigo_servicio = models.DecimalField(max_digits=10, decimal_places=0)
    persona_cargo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios_area'
        unique_together = (('codigo_area', 'codigo_servicio'),)


class ServiciosPrioridad(models.Model):
    codigo_servicio = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    prioridad = models.CharField(max_length=1)
    duracion = models.DecimalField(max_digits=5, decimal_places=0)
    unidad_medida = models.CharField(max_length=2)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios_prioridad'
        unique_together = (('codigo_servicio', 'prioridad'),)


class SiauDocumentos(models.Model):
    numero_documento = models.CharField(primary_key=True, max_length=50)
    tipo_documento = models.CharField(max_length=30)
    documento = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'siau_documentos'
        unique_together = (('numero_documento', 'tipo_documento'),)


class SiauMacroservicio(models.Model):
    codigo_macroservicio = models.IntegerField(primary_key=True)
    nombre_macroservicio = models.CharField(max_length=100)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'siau_macroservicio'


class SiauServicioSalud(models.Model):
    codigo_servicio = models.IntegerField(primary_key=True)
    nombre_servicio = models.CharField(max_length=100)
    codigo_macroservicio = models.ForeignKey(SiauMacroservicio, models.DO_NOTHING, db_column='codigo_macroservicio')
    codigo_servicio_general = models.CharField(max_length=20, blank=True, null=True)
    ambulatorio = models.CharField(max_length=1, blank=True, null=True)
    hospitalario = models.CharField(max_length=1, blank=True, null=True)
    unidad_movil = models.CharField(max_length=1, blank=True, null=True)
    domiciliario = models.CharField(max_length=1, blank=True, null=True)
    otras = models.CharField(max_length=1, blank=True, null=True)
    telemedicina_cr = models.CharField(max_length=1, blank=True, null=True)
    telemedicina_ir = models.CharField(max_length=1, blank=True, null=True)
    baja = models.CharField(max_length=1, blank=True, null=True)
    media = models.CharField(max_length=1, blank=True, null=True)
    alta = models.CharField(max_length=1, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'siau_servicio_salud'


class SisAplicaciones(models.Model):
    aplicacion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    modulo = models.CharField(primary_key=True, max_length=40)
    orden_aplicacion = models.DecimalField(max_digits=5, decimal_places=0)
    link_aplicacion = models.CharField(max_length=200, blank=True, null=True)
    tipo_aplicacion = models.CharField(max_length=1)
    menu_aplicacion = models.CharField(max_length=50, blank=True, null=True)
    ancho = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    alto = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    entorno = models.CharField(max_length=20, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=100)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_aplicaciones'
        unique_together = (('modulo', 'aplicacion'),)


class SisArchivos(models.Model):
    tabla = models.CharField(primary_key=True, max_length=50)
    secuencia = models.CharField(max_length=10)
    consecutivo = models.DecimalField(max_digits=5, decimal_places=0)
    archivo = models.CharField(max_length=200)
    estado = models.CharField(max_length=1, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_archivos'
        unique_together = (('tabla', 'secuencia', 'consecutivo'),)


class SisAyudas(models.Model):
    aplicacion = models.CharField(primary_key=True, max_length=40)
    pantalla = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=255)
    archivo_anexo = models.CharField(max_length=80, blank=True, null=True)
    tamano_anexo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=30, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_ayudas'
        unique_together = (('aplicacion', 'pantalla'),)


class SisBitacora(models.Model):
    consecutivo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    tabla = models.CharField(max_length=50, blank=True, null=True)
    llave1 = models.CharField(max_length=50, blank=True, null=True)
    llave2 = models.CharField(max_length=50, blank=True, null=True)
    llave3 = models.CharField(max_length=50, blank=True, null=True)
    llave4 = models.CharField(max_length=50, blank=True, null=True)
    llave5 = models.CharField(max_length=50, blank=True, null=True)
    accion = models.CharField(max_length=1, blank=True, null=True)
    campo = models.CharField(max_length=50, blank=True, null=True)
    val_inicial = models.CharField(max_length=4000, blank=True, null=True)
    val_final = models.CharField(max_length=4000, blank=True, null=True)
    usuario = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    observaciones = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_bitacora'


class SisCargos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=60)
    usuario_insercion = models.CharField(max_length=30)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_cargos'

    def __str__(self):
        return u'%s' % (self.descripcion)


class SisCarguesArchivos(models.Model):
    nombre_archivo = models.CharField(primary_key=True, max_length=80)
    leidos = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    insertados = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    actualizados = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    errores = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=1)
    estructura_usada = models.CharField(max_length=50)
    nombre_archivo_original = models.CharField(max_length=50, blank=True, null=True)
    solicitante = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=50)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=50, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_cargues_archivos'


class SisCarguesDetalle(models.Model):
    nombre_archivo = models.CharField(primary_key=True, max_length=80)
    numero_fila = models.DecimalField(max_digits=10, decimal_places=0)
    registro = models.CharField(max_length=2000)
    estado = models.CharField(max_length=1, blank=True, null=True)
    numero_errores = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    numero_advertencias = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    errores = models.CharField(max_length=4000, blank=True, null=True)
    advertencias = models.CharField(max_length=4000, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=50)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=50, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_cargues_detalle'
        unique_together = (('nombre_archivo', 'numero_fila'),)


class SisCiudades(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=60)
    usuario_insercion = models.CharField(max_length=30)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_ciudades'


class SisConsecutivos(models.Model):
    codigo_consecutivo = models.CharField(primary_key=True, max_length=50)
    valor_consecutivo = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_consecutivos'


class SisCorreos(models.Model):
    consecutivo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    origen = models.CharField(max_length=255)
    destino = models.CharField(max_length=50)
    asunto = models.CharField(max_length=255)
    mensaje = models.CharField(max_length=4000)
    estado = models.CharField(max_length=1)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    numero_solicitud = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    aplicacion = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_correos'


class SisEntidad(models.Model):
    nit_entidad = models.DecimalField(primary_key=True, max_digits=15, decimal_places=0)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    departamento = models.CharField(max_length=2, blank=True, null=True)
    municipio = models.CharField(max_length=3, blank=True, null=True)
    telefono = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=100)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_entidad'


class SisEstructuras(models.Model):
    estructura = models.CharField(primary_key=True, max_length=50)
    descripcion_estructura = models.CharField(max_length=80)
    formato = models.CharField(max_length=1)
    delimitador = models.CharField(max_length=1, blank=True, null=True)
    largo_registro = models.DecimalField(max_digits=4, decimal_places=0)
    estado = models.CharField(max_length=1)
    procedimiento_asociado = models.CharField(max_length=60)
    usuario_insercion = models.CharField(max_length=30)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    numero_registros_titulo = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    perfil_aplica = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_estructuras'


class SisEstructurasDetalle(models.Model):
    estructura = models.OneToOneField(SisEstructuras, models.DO_NOTHING, db_column='estructura', primary_key=True)
    campo = models.DecimalField(max_digits=3, decimal_places=0)
    descripcion = models.CharField(max_length=50)
    tipo_campo = models.CharField(max_length=1)
    obligatorio = models.CharField(max_length=1)
    longitud = models.DecimalField(max_digits=4, decimal_places=0)
    posicion_inicial = models.DecimalField(max_digits=4, decimal_places=0)
    posicion_final = models.DecimalField(max_digits=4, decimal_places=0)
    mensaje = models.CharField(max_length=100, blank=True, null=True)
    valor_minimo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    valor_maximo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_minima = models.DateTimeField(blank=True, null=True)
    fecha_maxima = models.DateTimeField(blank=True, null=True)
    rango_caracteres = models.CharField(max_length=30, blank=True, null=True)
    formato = models.CharField(max_length=3, blank=True, null=True)
    estado = models.CharField(max_length=1)
    usuario_insercion = models.CharField(max_length=30)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=30, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_estructuras_detalle'
        unique_together = (('estructura', 'campo'),)


class SisFuentesFinanciacion(models.Model):
    codigo_fuente = models.IntegerField(primary_key=True)
    codigo_recurso = models.ForeignKey('SisGruposRecursos', models.DO_NOTHING, db_column='codigo_recurso')
    nombre_fuente = models.CharField(max_length=100)
    estado_fuente = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_fuentes_financiacion'


class SisGrupos(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_grupos'


class SisGruposRecursos(models.Model):
    codigo_recurso = models.IntegerField(primary_key=True)
    nombre_recurso = models.CharField(max_length=60)
    estado_recurso = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_grupos_recursos'


class SisGruposUnidades(models.Model):
    codigo_grupo = models.IntegerField(primary_key=True)
    nombre_grupo = models.CharField(max_length=60)
    estado_grupo = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_grupos_unidades'


class SisLogin(models.Model):
    secuencia = models.DecimalField(primary_key=True, max_digits=15, decimal_places=0)
    usuario = models.CharField(max_length=60)
    fecha = models.DateTimeField()
    aplicacion = models.CharField(max_length=30, blank=True, null=True)
    metodo = models.CharField(max_length=1, blank=True, null=True)
    ip = models.CharField(max_length=25, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_login'


class SisMultivalores(models.Model):
    tabla = models.CharField(primary_key=True, max_length=50)
    valor = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    varios = models.CharField(max_length=200, blank=True, null=True)
    entero = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_multivalores'
        unique_together = (('tabla', 'valor'),)


class SisParametrosDoc(models.Model):
    id_parametro = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    asociado_a = models.CharField(max_length=1)
    estado = models.CharField(max_length=1, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_parametros_doc'


class SisPermisos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_permisos'


class SisPermisosGrupo(models.Model):
    grupo = models.OneToOneField(SisGrupos, models.DO_NOTHING, db_column='grupo', primary_key=True)
    permiso = models.ForeignKey(SisPermisos, models.DO_NOTHING, db_column='permiso')
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_permisos_grupo'
        unique_together = (('grupo', 'permiso'),)


class SisPlantillasDocumentos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=50)
    descripcion = models.CharField(max_length=60)
    documento = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_plantillas_documentos'


class SisRepresentante(models.Model):
    id_representante = models.IntegerField(primary_key=True)
    tipo_documento = models.CharField(max_length=10, blank=True, null=True)
    n_documento = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    expedicion = models.CharField(max_length=45, blank=True, null=True)
    nombre_1 = models.CharField(max_length=15, blank=True, null=True)
    nombre_2 = models.CharField(max_length=15, blank=True, null=True)
    apellido_1 = models.CharField(max_length=15, blank=True, null=True)
    apellido_2 = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    cargo = models.CharField(max_length=45, blank=True, null=True)
    titulo_profecion = models.CharField(max_length=45, blank=True, null=True)
    acta_nombramiento = models.CharField(max_length=45, blank=True, null=True)
    n_acta = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    fecha_acta = models.DateField(blank=True, null=True)
    periodo_inicial = models.DateField(blank=True, null=True)
    periodo_final = models.DateField(blank=True, null=True)
    nit_entidad = models.ForeignKey(SisEntidad, models.DO_NOTHING, db_column='nit_entidad', blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=100)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=3, blank=True, null=True)
    municipio = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_representante'


class SisSedes(models.Model):
    id_sede = models.IntegerField(primary_key=True)
    nit_entidad = models.ForeignKey(SisEntidad, models.DO_NOTHING, db_column='nit_entidad')
    nombre_sede = models.CharField(max_length=80)
    direccion = models.CharField(max_length=60)
    departamento = models.CharField(max_length=3, blank=True, null=True)
    municipio = models.CharField(max_length=3, blank=True, null=True)
    telefono = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=100)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_sedes'
        unique_together = (('id_sede', 'nit_entidad'),)


class SisUnidadesMedida(models.Model):
    codigo_unidad = models.CharField(primary_key=True, max_length=5)
    codigo_grupo = models.ForeignKey(SisGruposUnidades, models.DO_NOTHING, db_column='codigo_grupo')
    nombre_unidad = models.CharField(max_length=100)
    estado_unidad = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    factor_conversion = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'sis_unidades_medida'

    def __str__(self):
        return u'%s' % (self.nombre_unidad)


class SisUsuarios(models.Model):
    codigo_empleado = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    numero_identificacion = models.DecimalField(max_digits=10, decimal_places=0)
    tipo_identificacion = models.CharField(max_length=2)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    estado = models.CharField(max_length=1)
    password = models.CharField(max_length=30)
    idcorreo = models.CharField(max_length=30)
    email = models.CharField(max_length=80, blank=True, null=True)
    auditor_cordinador = models.CharField(max_length=1, blank=True, null=True)
    tipo_auditor = models.CharField(max_length=1, blank=True, null=True)
    usuario_supervisor = models.CharField(max_length=1, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    area = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    clase = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    supervisor = models.CharField(max_length=1, blank=True, null=True)
    cargo_generico = models.ForeignKey(SisCargos, models.DO_NOTHING, db_column='cargo_generico', blank=True, null=True)
    auditor_lider = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_usuarios'


class SisUsuariosArea(models.Model):
    codigo_area = models.OneToOneField('UnidadesDependencia', models.DO_NOTHING, db_column='codigo_area', primary_key=True)
    codigo_empleado = models.DecimalField(max_digits=10, decimal_places=0)
    clase = models.ForeignKey(SisGrupos, models.DO_NOTHING, db_column='clase')
    responsable_area = models.CharField(max_length=1)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    area_principal = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis_usuarios_area'
        unique_together = (('codigo_area', 'codigo_empleado'),)


class Solicitudes(models.Model):
    numero = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    fecha_generada = models.DateTimeField()
    area_cliente = models.ForeignKey('UnidadesDependencia', models.DO_NOTHING, db_column='area_cliente', related_name='+')
    empleado_cliente = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_servicio = models.ForeignKey(Servicios, models.DO_NOTHING, db_column='codigo_servicio')
    area_proveedor = models.ForeignKey('UnidadesDependencia', models.DO_NOTHING, db_column='area_proveedor', blank=True, null=True, related_name='+')
    empleado_proveedor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    codigo_estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='codigo_estado')
    abierta = models.CharField(max_length=1)
    nivel_escalamiento = models.DecimalField(max_digits=3, decimal_places=0)
    fecha_vigencia = models.DateTimeField(blank=True, null=True)
    fecha_estimada_terminacion = models.DateTimeField(blank=True, null=True)
    fecha_real_terminacion = models.DateTimeField(blank=True, null=True)
    fecha_base_escalamientos = models.DateTimeField(blank=True, null=True)
    solicitud_padre = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    codigo_oportunidad = models.CharField(max_length=1, blank=True, null=True)
    fecha_oportunidad = models.DateTimeField(blank=True, null=True)
    codigo_confiabilidad = models.CharField(max_length=1, blank=True, null=True)
    fecha_confiabilidad = models.DateTimeField(blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    encuesta = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    duracion = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    unidad_medida = models.CharField(max_length=5, blank=True, null=True)
    proveedor_anterior = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    notificar = models.CharField(max_length=1, blank=True, null=True)
    ciclo = models.CharField(max_length=6, blank=True, null=True)
    empleado_auditor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tipo_calificacion_auditor = models.CharField(max_length=1, blank=True, null=True)
    numero_devoluciones = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    estado_anterior = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    macro_servicio = models.CharField(max_length=1, blank=True, null=True)
    secuencia_externa = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    numero_macroservicio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    numero_flujo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    codigo_flujo = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    cerrar_solicitud = models.CharField(max_length=1, blank=True, null=True)
    empleado_escalo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    fecha_ult_escalamiento = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitudes'


class SolicitudesMacro(models.Model):
    numero_macroservicio = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    numero_solicitud = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_insercion = models.DateTimeField()
    usuario_insercion = models.CharField(max_length=60)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitudes_macro'
        unique_together = (('numero_macroservicio', 'numero_solicitud'),)


class SolicitudesPeriodo(models.Model):
    periodo = models.CharField(primary_key=True, max_length=6)
    numero = models.DecimalField(max_digits=10, decimal_places=0)
    tipo_solicitud = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_generada = models.DateTimeField()
    area_cliente = models.DecimalField(max_digits=10, decimal_places=0)
    empleado_cliente = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_servicio = models.DecimalField(max_digits=10, decimal_places=0)
    area_proveedor = models.DecimalField(max_digits=10, decimal_places=0)
    empleado_proveedor = models.DecimalField(max_digits=10, decimal_places=0)
    codigo_estado = models.DecimalField(max_digits=10, decimal_places=0)
    abierta = models.CharField(max_length=1)
    nivel_escalamiento = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_vigencia = models.DateTimeField(blank=True, null=True)
    fecha_estimada_terminacion = models.DateTimeField(blank=True, null=True)
    fecha_real_terminacion = models.DateTimeField(blank=True, null=True)
    fecha_base_escalamientos = models.DateTimeField(blank=True, null=True)
    solicitud_padre = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    codigo_oportunidad = models.CharField(max_length=1, blank=True, null=True)
    fecha_oportunidad = models.DateTimeField(blank=True, null=True)
    codigo_confiabilidad = models.CharField(max_length=1, blank=True, null=True)
    fecha_confiabilidad = models.DateTimeField(blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    encuesta = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    estadoplandigalo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    duracion = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    unidad_medida = models.IntegerField(blank=True, null=True)
    proveedor_anterior = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    notificar = models.CharField(max_length=1, blank=True, null=True)
    ciclo = models.CharField(max_length=6, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    empleado_auditor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tipo_calificacion_auditor = models.CharField(max_length=1, blank=True, null=True)
    numero_devoluciones = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    estado_anterior = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    macro_servicio = models.CharField(max_length=1, blank=True, null=True)
    secuencia_externa = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitudes_periodo'
        unique_together = (('periodo', 'numero'),)


class Subprocesos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=20)
    proceso = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=120)
    estado = models.CharField(max_length=1, blank=True, null=True)
    factor = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codigo_homologado = models.CharField(max_length=2, blank=True, null=True)
    estado_homologacion = models.CharField(max_length=1, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subprocesos'
        unique_together = (('codigo', 'proceso'),)

    def __str__(self):
        return u'%s %s' % (self.codigo, self.descripcion)


class TableromandoIndicador(models.Model):
    estado = models.BooleanField()
    tipo = models.SmallIntegerField()
    consecutivo = models.IntegerField()
    nombre_identificador = models.CharField(max_length=300, blank=True, null=True)
    objetivo = models.TextField(blank=True, null=True)
    producto_mide = models.TextField(blank=True, null=True)
    tipo_medicion = models.SmallIntegerField()
    ciclo = models.SmallIntegerField()
    periodicidad = models.SmallIntegerField()
    ambito = models.SmallIntegerField()
    dimension = models.SmallIntegerField()
    responsable = models.SmallIntegerField()
    normatividad = models.CharField(max_length=10)
    fecha_registro = models.DateTimeField()
    fecha_modificacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    limite_reporte = models.SmallIntegerField()
    version = models.FloatField()
    recurrencia = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'tableroMando_indicador'


class TableromandoMedicion(models.Model):
    indicador = models.OneToOneField(TableromandoIndicador, models.DO_NOTHING, primary_key=True)
    tipo_formula = models.SmallIntegerField()
    unidad_medicion = models.SmallIntegerField()
    tendencia = models.SmallIntegerField()
    archivo_asociado = models.CharField(max_length=100, blank=True, null=True)
    nombre_variable_1 = models.CharField(max_length=200)
    nomenclaruta_1 = models.CharField(max_length=6)
    unidad_1 = models.SmallIntegerField(blank=True, null=True)
    fuente_1 = models.CharField(max_length=100, blank=True, null=True)
    nombre_variable_2 = models.CharField(max_length=200, blank=True, null=True)
    nomenclaruta_2 = models.CharField(max_length=6, blank=True, null=True)
    unidad_2 = models.SmallIntegerField(blank=True, null=True)
    fuente_2 = models.CharField(max_length=100, blank=True, null=True)
    nombre_respuesta = models.CharField(max_length=200, blank=True, null=True)
    nomenclaruta_respuesta = models.CharField(max_length=6, blank=True, null=True)
    unidad_respuesta = models.SmallIntegerField(blank=True, null=True)
    fuente_respuesta = models.CharField(max_length=100, blank=True, null=True)
    formula = models.TextField()
    interpretacion_resultado = models.TextField(blank=True, null=True)
    rango_inicial = models.IntegerField(blank=True, null=True)
    rango_final = models.IntegerField(blank=True, null=True)
    responsable_reporte = models.SmallIntegerField(blank=True, null=True)
    responsable_consolidacion = models.SmallIntegerField(blank=True, null=True)
    responsable_analisis_seguimiento = models.SmallIntegerField(blank=True, null=True)
    responsable_decisiones = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tableroMando_medicion'


class TipoAuditor(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_auditor'


class TiposCalificacion(models.Model):
    codigo = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=40)
    valor = models.DecimalField(max_digits=10, decimal_places=0)
    rango_inicial = models.DecimalField(max_digits=10, decimal_places=0)
    rango_final = models.DecimalField(max_digits=10, decimal_places=0)
    justifica = models.CharField(max_length=1)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=0)
    indice_satisfaccion = models.CharField(max_length=200)
    rango_inicial_indice = models.DecimalField(max_digits=10, decimal_places=0)
    rango_final_indice = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_calificacion'


class TiposEstado(models.Model):
    codigo = models.CharField(primary_key=True, max_length=3)
    descripcion = models.CharField(max_length=40)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_estado'


class TiposServicios(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_servicios'


class TiposSolicitud(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=40)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_solicitud'


class UnidadesDependencia(models.Model):
    codigo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=80)
    nivel_superior = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    persona_responsable = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    estado = models.CharField(max_length=1)
    nivel = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    secuencia = models.CharField(max_length=50, blank=True, null=True)
    anidar = models.CharField(max_length=1, blank=True, null=True)
    ubicacion = models.CharField(max_length=60, blank=True, null=True)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    incluir_calidad = models.CharField(max_length=1, blank=True, null=True)
    modifica_especificos = models.CharField(max_length=1, blank=True, null=True)
    permite_actas = models.CharField(max_length=1, blank=True, null=True)
    modifica_logros = models.CharField(max_length=1, blank=True, null=True)
    codigo_tutor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    lider_acciones_mejora = models.CharField(max_length=1, blank=True, null=True)
    tipo_area = models.CharField(max_length=1, blank=True, null=True)
    municipio_ubicacion = models.CharField(max_length=3, blank=True, null=True)
    nivel_organigrama = models.CharField(max_length=5, blank=True, null=True)
    area_agrupa = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    ciclo_auditoria = models.CharField(max_length=6, blank=True, null=True)
    ciclo_anterior = models.CharField(max_length=6, blank=True, null=True)
    plan_especial = models.CharField(max_length=1, blank=True, null=True)
    codigo_externo = models.CharField(max_length=6, blank=True, null=True)
    departamento_ubicacion = models.ForeignKey(ParDepartamento, models.DO_NOTHING, db_column='departamento_ubicacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidades_dependencia'


class UnidadesMedida(models.Model):
    codigo = models.CharField(primary_key=True, max_length=2)
    descripcion = models.CharField(max_length=40)
    factor_conversion = models.DecimalField(max_digits=10, decimal_places=0)
    usuario_insercion = models.CharField(max_length=60, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidades_medida'


class WkfAcciones(models.Model):
    codigo_accion = models.DecimalField(primary_key=True, max_digits=6, decimal_places=0)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=1)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf_acciones'


class WkfDetalle(models.Model):
    codigo_flujo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    secuencia = models.DecimalField(max_digits=5, decimal_places=0)
    servicio_inicio = models.DecimalField(max_digits=10, decimal_places=0)
    accion = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    codigo_estado = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    servicio_destino = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    nombre_procedimiento = models.CharField(max_length=61, blank=True, null=True)
    correo_destino = models.CharField(max_length=61, blank=True, null=True)
    estado = models.CharField(max_length=1)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    enviar_solicitud = models.CharField(max_length=1, blank=True, null=True)
    caracteristica = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    valor_caracteristica = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    caracteristica_correo = models.CharField(max_length=80, blank=True, null=True)
    ind_mismo_proveedor = models.CharField(max_length=1, blank=True, null=True)
    ind_mismo_cliente = models.CharField(max_length=1, blank=True, null=True)
    metodo_seleccion_proveedor = models.CharField(max_length=30, blank=True, null=True)
    ind_correo_clientes = models.CharField(max_length=1, blank=True, null=True)
    enviar_hermana = models.CharField(max_length=1, blank=True, null=True)
    enviar_si_hermana_cerrada = models.CharField(max_length=1, blank=True, null=True)
    ind_cliente_inicial = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf_detalle'
        unique_together = (('codigo_flujo', 'secuencia'),)


class WkfFlujoIniciado(models.Model):
    numero = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    codigo_flujo = models.DecimalField(max_digits=4, decimal_places=0)
    estado = models.CharField(max_length=1)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    numero_solicitud = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf_flujo_iniciado'


class WkfFlujos(models.Model):
    codigo_flujo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=100)
    servicio_inicial = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=1)
    usuario_insercion = models.CharField(max_length=60)
    fecha_insercion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=60, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf_flujos'
