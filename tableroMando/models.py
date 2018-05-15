from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from multiselectfield import MultiSelectField
from ge1.models import SisCargos, SisUnidadesMedida

GERENTE = 1
SUBGERENTE_ADMINISTRATIVO = 2
SUBGERENTE_CIENTIFICO = 3
COORDINADOR_1 = 4
COORDINADOR_2 = 5
COORDINADOR_3 = 6

RESPONSABLE_OPCIONES = (
	(GERENTE, 'Gerente'),
	(SUBGERENTE_ADMINISTRATIVO, 'Subgerente administrativo'),
	(SUBGERENTE_CIENTIFICO, 'Subgerente cientifico'),
	(COORDINADOR_1, 'Coordinador 1'),
	(COORDINADOR_2, 'Coordinador 2'),
	(COORDINADOR_3, 'Coordinador 3'),
)

class Indicador(models.Model):

# IDENTIFICADOR
	PLAN_DE_DESARROLLO = 1
	SISTEMA_DE_SALUD = 2
	SISTEMA_DE_GESTION = 3
	FINANCIERO = 4

	ABREBIATURA_INDICADORES = (
		(PLAN_DE_DESARROLLO, 'PDI'),
		(SISTEMA_DE_SALUD, 'SSS'),
		(SISTEMA_DE_GESTION, 'SGC'),
		(FINANCIERO, 'FIN'),
	)

	TIPO_INDICADOR_OPCIONES = (
		(PLAN_DE_DESARROLLO, 'Plan de desarrollo'),
		(SISTEMA_DE_SALUD, 'Sistema de salud'),
		(SISTEMA_DE_GESTION, 'Sistema de gestion'),
		(FINANCIERO, 'Financiero'),
	)
	
	# PIB = 'PIB'
	# NBI = 'NBI'
	# TDE = 'TDE'
	# PEA = 'PEA'

	# NOMENCLADOR_OPCIONES = (
	# 	(PIB, 'Producto Interno Bruto'),
	# 	(NBI, 'Necesidades Basicas Insatisfechas'),
	# 	(TDE, 'Tasa de Desercion Escolar'),
	# 	(PEA, 'Poblacion Economicamente Activa'),
	# )

	MANUAL = 1
	AUTOMATICO = 2
	TIPOS_MEDICIONES = (
		(MANUAL, 'Manual'),
		(AUTOMATICO, 'Automatico'),
	)

	ANUAL = 1
	BIENAL = 2
	TRIENAL = 3
	CUATRIENAL = 4
	QUINQUENAL = 5
	DECENAL = 10

	CICLO_OPCIONES = (
		(ANUAL, 'Anual'),
		(BIENAL, 'Bienal'),
		(TRIENAL, 'Trienal'),
		(CUATRIENAL,'Cuatrienal'),
		(QUINQUENAL, 'Quinquenal'),
		(DECENAL, 'Decenal'),

	)

	# DIARIO = 1
	# SEMANAL = 2
	# QUINCENAL = 3
	MENSUAL = 4
	BIMENSUAL = 5 
	TRIMESTRAL = 6
	CUATRIMESTRAL = 7
	SEMESTRAL = 8
	ANUAL = 9
	# BIENAL = 10
	# TRIENAL = 11
	# CUATRIENAL = 12
	# OTRO = 13

	PERIODICIDAD_OPCIONES = (
		# (DIARIO, 'Diario'),
		# (SEMANAL, 'Semanal'),
		# (QUINCENAL, 'Quincenal'),
		(MENSUAL, 'Mensual'),
		(BIMENSUAL, 'Bimensual'),
		(TRIMESTRAL, 'Trimestral'),
		(CUATRIMESTRAL, 'Cuatrimestral'),
		(SEMESTRAL, 'Semestral'),
		(ANUAL, 'Anual'),
		# (BIENAL, 'Bienal'),
		# (TRIENAL, 'Trienal'),
		# (CUATRIENAL, 'Cuatrienal'),
		# (OTRO, 'Otro'),
	)

	IMPACTO = 1
	GESTION = 2
	RESULTADO = 3
	PROCESO = 4
	PRODUCTO = 5
	EFECTO = 6
	ACCION = 7
	RECURSO = 8

	AMBITOS = (
		(IMPACTO, 'Impacto'),
		(GESTION, 'Gestion'),
		(RESULTADO, 'Resultado'),
		(PROCESO, 'Proceso'),
		(PRODUCTO, 'Producto'),
		(EFECTO, 'Efecto'),
		(ACCION, 'Accion'),
		(RECURSO, 'Recurso'),
	)

	EFICACIA = 1
	EFICIENCIA = 2
	EFECTIVIDAD = 3
	ECONOMIA = 4
	SEGURIDAD = 5
	CALIDAD = 6
	ATENCION = 7
	EQUIDAD = 8

	DIMENCIONES = (
		(EFICACIA, 'Eficacia'),
		(EFICIENCIA, 'Eficiencia'),
		(EFECTIVIDAD, 'Efectividad'),
		(ECONOMIA, 'Economia'),
		(SEGURIDAD, 'Seguridad'),
		(CALIDAD, 'Calidad'),
		(ATENCION, 'Atencion'),
		(EQUIDAD, 'Equidad'),
	)

	RESOLUCION_256 = 1
	RESOLUCION_742 = 2
	DECRETO_2193 = 3
	RESOLUCION_1552 = 4
	CIRCULAR_030 = 5
	NORMATIVIDAD_INTERNA = 6
	NORMATIVIDAD_OPCIONES = (
		(RESOLUCION_256, 'Resolucion 256'),
		(RESOLUCION_742, 'Resolucion 743'),
		(DECRETO_2193, 'Decreto 2193'),
		(RESOLUCION_1552, 'Resolución 1552'),
		(CIRCULAR_030, 'Circular 030'),
		(NORMATIVIDAD_INTERNA, 'Normatividad Interna'),
	)

	PRIMERO = 1
	SEGUNDO = 2
	TERCERO = 3
	CUARTO = 4
	QUINTO = 5
	SEXTO = 6
	SEPTIMO = 7 
	OCTAVO = 8
	NOVENO = 9
	DECIMO = 10
	QUINCE = 15
	VEINTE = 20
	VEINTI_CINCO = 25
	ULTIMO_DIA_MES = 28

	LIMITES_REPORTES = (
		(PRIMERO, 'Primero día hábil del siguiente periodo'),
		(SEGUNDO, 'Segundo día hábil del siguiente periodo'),
		(TERCERO, 'Tercero día hábil del siguiente periodo'),
		(CUARTO, 'Cuarto día hábil del siguiente periodo'),
		(QUINTO, 'Quinto día hábil del siguiente periodo'),
		(SEXTO, 'Sexto día hábil del siguiente periodo'),
		(SEPTIMO, 'Septimo día hábil del siguiente periodo'),
		(OCTAVO, 'Octavo día hábil del siguiente periodo'),
		(NOVENO, 'Noveno día hábil del siguiente periodo'),
		(DECIMO, 'Decimo día hábil del siguiente periodo'),
		(QUINCE, 'Día quince del siguiente periodo'),
		(VEINTE, 'Día veinte del siguiente periodo'),
		(VEINTI_CINCO, 'Día veinti cinco del siguiente periodo'),
		(ULTIMO_DIA_MES, 'Día ultimo dia mes del siguiente periodo'),
	)

	estado				= models.BooleanField(default=True)  #  estado para inactivar en caso de eliminar	
	tipo_indicador 		= MultiSelectField(max_length=10,choices=TIPO_INDICADOR_OPCIONES, default="")
	consecutivo			= models.IntegerField()
	nombre_identificador= models.CharField(max_length = 300,blank=True, null=True)
	objetivo  			= models.TextField(blank=True, null=True)
	producto_mide		= models.TextField(blank=True, null=True)
	tipo_medicion		= models.SmallIntegerField(choices=TIPOS_MEDICIONES, default=MANUAL)
	ciclo				= models.SmallIntegerField(choices=CICLO_OPCIONES, default=CUATRIENAL)
	periodicidad		= models.SmallIntegerField(choices=PERIODICIDAD_OPCIONES, default=SEMESTRAL)
	ambito				= models.SmallIntegerField(choices=AMBITOS, default=RESULTADO)
	dimension			= models.SmallIntegerField(choices=DIMENCIONES, default=EFICACIA)
	responsable			= models.ForeignKey(SisCargos, on_delete=models.DO_NOTHING)
	normatividad 		= MultiSelectField(max_length=10,choices=NORMATIVIDAD_OPCIONES)
	fecha_registro		= models.DateTimeField(editable=False) #DateTimeField(default=timezone.now) -- DateField()
	fecha_modificacion	= models.DateTimeField() # Esta fecha se eactualiza cada vez que se actualiza
	fecha_actualizacion	= models.DateTimeField()
	limite_reporte   	= models.SmallIntegerField(choices=LIMITES_REPORTES, default=SEGUNDO)
	version    			= models.FloatField(default="1")
	recurrencia			= models.NullBooleanField(default=True)
	verificado 			= models.BooleanField(default=False)
	# tipo	  			= models.SmallIntegerField(choices=TIPO_INDICADOR_OPCIONES, default=PLAN_DE_DESARROLLO)
	# nomenclador			= models.CharField(choices=NOMENCLADOR_OPCIONES, max_length = 3, default=TDE)
	# usuario_registro 	= models.ForeignKey(User, on_delete=models.DO_NOTHING)

	# ARMONIZACION
	
	# def get_prefijo(self):
	# 	return self.ABREBIATURA_INDICADORES[self.tipo-1][1]


	def str_codigo(self):
		return u'IND - %s' % (self.consecutivo)


	def save(self, *args, **kwargs):
		if not self.id:
			self.fecha_registro = timezone.now()
			self.fecha_actualizacion = timezone.now()
		self.fecha_modificacion = timezone.now()
		return super(Indicador, self).save(*args, **kwargs)	


	# def get_medicion(self):
	# 	return Medicion.objects.get()


	def __str__(self):
		return u'IND - %s %s' % (self.consecutivo, self.nombre_identificador)



class Medicion(models.Model):
	#MEDICION
	PORCENTAJE = 1
	TASA_VARIACION = 2
	PROMEDIO = 3
	NUMERO_ENTERO = 4

	TIPOS_FORMULA = (
		(PORCENTAJE, 'Porcentaje'),
		(TASA_VARIACION, 'Tasa de variación'),
		(PROMEDIO, 'Promedio'),
		(NUMERO_ENTERO, 'Numero entero'),
	)

	INCREMENTO = 1
	MANTENIMIENTO = 2
	DISMINUCION = 3

	TENCENCIAS_MEDICION = (
		(INCREMENTO, 'Incremento'),
		(MANTENIMIENTO, 'Mantenimiento'),
		(DISMINUCION, 'Disminucion'),
	)

	UN_PORCENTAJE = 1
	UNIDADES = (
		(UN_PORCENTAJE, 'Porcentaje'),
	)

	FORMULAS_PREDETERMINADAS = (
		(TASA_VARIACION, '$$TDE = {NEAG(Tn) - NEAG(T0) \over NEAG(T0) }X 100$$'),
		(PORCENTAJE, '$$TDE = {NEAG \over NEM }X 100$$'),
		(PROMEDIO, '$$TDE = {NEC \over NGC }$$'),
		(NUMERO_ENTERO, '$$TDE = {NEC}$$'),
	)

	indicador 			= models.OneToOneField(Indicador, on_delete=models.CASCADE, primary_key=True)
	tipo_formula 		= models.SmallIntegerField(choices=TIPOS_FORMULA, default=TASA_VARIACION)
	unidad_medicion		= models.ForeignKey(SisUnidadesMedida, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='+')
	tendencia 			= models.SmallIntegerField(choices=TENCENCIAS_MEDICION, default=INCREMENTO)
	archivo_asociado 	= models.CharField(max_length = 100, blank=True, null=True)

	nombre_variable_1	= models.CharField(max_length = 200)
	nomenclaruta_1 		= models.CharField(max_length = 6)
	unidad_1			= models.ForeignKey(SisUnidadesMedida, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='+')
	fuente_1			= models.CharField(max_length = 100, blank=True, null=True)

	nombre_variable_2	= models.CharField(max_length = 200, blank=True, null=True)
	nomenclaruta_2 		= models.CharField(max_length = 6, blank=True, null=True)
	unidad_2			= models.ForeignKey(SisUnidadesMedida, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='+')
	fuente_2			= models.CharField(max_length = 100, blank=True, null=True)

	nombre_respuesta	= models.CharField(max_length = 200, blank=True, null=True)
	nomenclaruta_respuesta = models.CharField(max_length = 6, blank=True, null=True)
	unidad_respuesta	= models.ForeignKey(SisUnidadesMedida, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='+')
	fuente_respuesta	= models.CharField(max_length = 100, blank=True, null=True)

	formula 			= models.TextField()
	
	interpretacion_resultado = models.TextField(blank=True, null=True)
	rango_inicial 		= models.IntegerField(blank=True, null=True)
	rango_final 		= models.IntegerField(blank=True, null=True)
	responsable_reporte = models.ForeignKey(SisCargos, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='+')
	responsable_consolidacion = models.ForeignKey(SisCargos, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='+')
	responsable_analisis_seguimiento = models.ForeignKey(SisCargos, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='+')
	responsable_decisiones = models.ForeignKey(SisCargos, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='+')

	def __str__(self):
		return u'%s -- %s' % (self.indicador, self.tipo_formula)


from ge1.models import PdeMetas, Procesos, Subprocesos, PdeUnidadNivel, SisMultivalores
class Armonizacion(models.Model):
	ESTRATEGICO = 1
	MISIONAL = 2
	APOYO = 3
	EVALUACION = 4

	TIPOS_PROCESOS = (
		(ESTRATEGICO, 'Estrategico'),
		(MISIONAL, 'Misional'),
		(APOYO, 'Apoyo'),
		(EVALUACION, 'Evaluacion'),
	)

	indicador = models.OneToOneField(Indicador, on_delete=models.DO_NOTHING, primary_key=True)
	# Plan de desarrollo
	linea = models.ForeignKey(PdeUnidadNivel, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='+')
	programa = models.ForeignKey(PdeUnidadNivel, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='+')
	subprograma = models.ForeignKey(PdeUnidadNivel, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='+')

	meta = models.ForeignKey(PdeMetas, on_delete=models.DO_NOTHING, blank=True, null=True)

	# Sistema integrado de gestion
	tipo_proceso = models.SmallIntegerField(choices=TIPOS_PROCESOS, default=ESTRATEGICO, blank=True)
	proceso = models.ForeignKey(Procesos, on_delete=models.DO_NOTHING, blank=True, null=True)
	# subproceso = models.ForeignKey(Subprocesos, on_delete=models.DO_NOTHING, blank=True, null=True)

	def __str__(self):
		return u'id -- %s' % (self.indicador.id)

