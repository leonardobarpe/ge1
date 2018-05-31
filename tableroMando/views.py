from django.shortcuts import render
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse, render
from django.template import RequestContext
from tableroMando.forms import *
from tableroMando.models import *
from django.contrib.auth.models import User
from datetime import datetime, date, timedelta
from django.urls import reverse
from django.views.generic import View
from ge1.models import PdePlanDesarrollo
from django.db.models import Max, Min
import json

def inicioTableroMando(request):
	return render_to_response('inicioTableroMando.html', locals())


def programacion(request):
	return render_to_response('programacion.html', locals())


def seguimiento(request):
	return render_to_response('seguimiento.html', locals())



class ConfiguracionIndicador(View):

	ACCION_AGREGAR = 'agregar'
	TEMPLATE_AGREGAR = 'nuevo_indicador.html'

	ACCION_AGREGAR_MEDICION = 'agregar_m'
	ACCION_AGREGAR_ARMONIZACION = 'agregar_a'

	ACCION_LISTAR = 'listar_i'
	TEMPLATE_LISTAR = 'listar_indicadores.html'

	ACCION_ELIMINAR = 'eliminar'
	ACCION_VERIFICAR = 'verificar'
	ACCION_AGREGAR_PROGRAMACION = 'agregar_progra'


	def agregar_indicador(self, request):
		formulario = IndicadorFormulario(request.POST or None)
		abrebiatura_indicadores = Indicador.ABREBIATURA_INDICADORES

		indicador = None
		if 'indicador' in request.GET:
			indicador = Indicador.objects.get(pk=request.GET['indicador'])

		form_medicion = MedicionForm(request.POST or None)
		form_armonizacion = ArmonizacionForm(request.POST or None)

		try:
			medicion = Medicion.objects.get(indicador=indicador)
		except Medicion.DoesNotExist:
			medicion = None
			pass

		try:
			armonizacion = Armonizacion.objects.get(indicador=indicador)
		except Armonizacion.DoesNotExist:
			armonizacion = None
			pass

		if formulario.is_valid():
			if not indicador:
				nuevo_i = formulario.save(commit=False)
				# nuevo_i.usuario_registro = User.objects.get(pk=request.user.id)
				nuevo_i.save()
				return HttpResponseRedirect('/tablero-Mando/indicador/?agregar&indicador=%s' % nuevo_i.pk)
			else:
				indicador.tipo_indicador = formulario.cleaned_data.get('tipo_indicador')
				indicador.consecutivo = formulario.cleaned_data.get('consecutivo')
				indicador.nombre_identificador = formulario.cleaned_data.get('nombre_identificador')
				indicador.objetivo = formulario.cleaned_data.get('objetivo')
				indicador.producto_mide = formulario.cleaned_data.get('producto_mide')
				indicador.ciclo = formulario.cleaned_data.get('ciclo')
				indicador.periodicidad = formulario.cleaned_data.get('periodicidad')
				indicador.ambito = formulario.cleaned_data.get('ambito')
				indicador.dimension = formulario.cleaned_data.get('dimension')
				indicador.responsable = formulario.cleaned_data.get('responsable')
				indicador.normatividad = formulario.cleaned_data.get('normatividad')
				indicador.limite_reporte = formulario.cleaned_data.get('limite_reporte')
				indicador.fecha_actualizacion = formulario.cleaned_data.get('fecha_actualizacion')
				# indicador.version = formulario.cleaned_data.get('version')
				# indicador.tipo_medicion = formulario.cleaned_data.get('tipo_medicion')
				# indicador.recurrencia = formulario.cleaned_data.get('recurrencia')
				indicador.save()
				return HttpResponseRedirect('/tablero-Mando/indicador/?agregar&indicador=%s' % indicador.pk)

		return render(request, self.TEMPLATE_AGREGAR, locals())


	def agregar_medicion(self, request):
		indicador = Indicador.objects.get(pk=request.GET['indicador'])
		form_medicion = MedicionForm(request.POST or None)
		if form_medicion.is_valid():
			nuevo_m = form_medicion.save(commit=False)
			nuevo_m.indicador = indicador
			nuevo_m.save()
			return HttpResponseRedirect('/tablero-Mando/indicador/?agregar&indicador=%s' % indicador.pk)
		return render(request, self.TEMPLATE_AGREGAR, locals())


	def agregar_armonizacion(self, request):
		indicador = Indicador.objects.get(pk=request.GET['indicador'])
		form_armonizacion = ArmonizacionForm(request.POST or None)
		if form_armonizacion.is_valid():
			nuevo_a = form_armonizacion.save(commit=False)
			nuevo_a.indicador = indicador
			nuevo_a.save()
			return HttpResponseRedirect('/tablero-Mando/indicador/?agregar&indicador=%s' % indicador.pk)
		return render(request, self.TEMPLATE_AGREGAR, locals())


	def listar_indicadores(self, request):
		indicadores = Indicador.objects.filter(estado=True)
		return render(request, self.TEMPLATE_LISTAR, locals())


	def eliminar_indicador(self, request):
		indicador = Indicador.objects.get(pk=request.GET['indicador'])
		indicador.estado = False
		indicador.save()
		return HttpResponseRedirect('/tablero-Mando/indicador/?listar_i')

	def verificar_indicador(self, request):
		indicador = Indicador.objects.get(pk=request.GET['indicador'])
		indicador.verificado = True
		indicador.save()
		return HttpResponseRedirect('/tablero-Mando/indicador/?listar_i')


	def agregar_programacion_ajax(self, request):
		if request.is_ajax():
			respuesta['mensaje'] = (u'Se han almacenado.')
			return HttpResponse(json.dumps(respuesta))
		else:
			return HttpResponse("peticion invalida, not ajax", status=403)


	def get(self, request):
		if self.ACCION_AGREGAR in request.GET:
			return self.agregar_indicador(request)

		if self.ACCION_LISTAR in request.GET:
			return self.listar_indicadores(request)

		if self.ACCION_ELIMINAR in request.GET:
			return self.eliminar_indicador(request)

		if self.ACCION_VERIFICAR in request.GET:
			return self.verificar_indicador(request)

		return HttpResponse("peticion invalida", status=403)


	def post(self, request):
		if self.ACCION_AGREGAR in request.GET:
			return self.agregar_indicador(request)

		if self.ACCION_AGREGAR_MEDICION in request.GET:
			return self.agregar_medicion(request)

		if self.ACCION_AGREGAR_ARMONIZACION in request.GET:
			return self.agregar_armonizacion(request)

		if self.ACCION_AGREGAR_PROGRAMACION in request.GET:
			return self.agregar_programacion_ajax(request)

		return HttpResponse("peticion invalida", status=403)


from ge1.models import SisFuentesFinanciacion
class ProgramacionIndicador(View):
	VER_PROGRAMACION = 'ver_base'
	TEMPLATE_VER_PROGRAMACION = 'programacion/ver_programacion.html'

	AGREGAR_FUENTE_FINANCIACION ='agregar_ff'
	AGREGAR_SISTEMA_INTEGRADO_GESTION = 'agregar_sig'

	def ver_informacion_base(self, request):
		indicador = Indicador.objects.get(pk=request.GET['i'])
		planes_desarrollo = PdePlanDesarrollo.objects.aggregate(max_date=Max('fecha_inicial'), min_date=Min('fecha_final'))

		print(("MAX: %s Min: %s ") % (planes_desarrollo['max_date'], planes_desarrollo['min_date']))

		periodos = PERIODICIDAD_OPCIONES
		sisfuentesfinanciacion = SisFuentesFinanciacion.objects.all()
		try:
			fuente_financiacion = FuenteFinanciacion.objects.get(indicador=indicador, estado=True)
		except FuenteFinanciacion.DoesNotExist:
			pass

		try:
			sistema_integrado_gestion = SistemaIntegradoGestion.objects.get(indicador=indicador, estado=True)
		except SistemaIntegradoGestion.DoesNotExist:
			pass

		return render_to_response(self.TEMPLATE_VER_PROGRAMACION, locals())


	def agregar_fuente_financiacion_ajax(self, request):
		respuesta = {}
		if request.is_ajax():
			indicador = Indicador.objects.get(pk=request.POST['indicador'])
			fuentes = request.POST.getlist('fuentes[]')

			try:
				fuente_financiacion = FuenteFinanciacion.objects.get(indicador=indicador, estado=True)
			except FuenteFinanciacion.DoesNotExist:
				fuente_financiacion = FuenteFinanciacion()
				pass

			fuente_financiacion.indicador = indicador
			fuente_financiacion.linea_base = request.POST['linea_base']
			fuente_financiacion.meta_periodo = request.POST['meta_periodo']
			fuente_financiacion.save()

			if (fuente_financiacion.item_fuente_financiacion.count() > 0):
				fuente_financiacion.item_fuente_financiacion.all().delete()
			for f in fuentes:
				dicc = json.loads(f)
				val_id_fuente = int(dicc['id_fuente'])
				val_anio = int(dicc['anio'])
				if(val_id_fuente > 0 and val_anio > 0):
					item = ItemFuenteFinanciacion()
					item.fuente = SisFuentesFinanciacion.objects.get(pk=val_id_fuente)
					item.anio = val_anio
					item.valor = float(dicc['valor_fuete'])
					item.save()
					fuente_financiacion.item_fuente_financiacion.add(item)
					fuente_financiacion.save()

			respuesta['mensaje'] = "Se almaceno la fuente de financiacion correctamente"
			return HttpResponse(json.dumps(respuesta))
		else:
			return HttpResponse("peticion invalida, not ajax", status=403)


	def agregar_sistema_integrado_gestion(self, request):
		respuesta = {}
		if request.is_ajax():
			indicador = Indicador.objects.get(pk=request.POST['indicador'])
			sistemas = request.POST.getlist('sistemas[]')

			try:
				sistema_integrado_gestion = SistemaIntegradoGestion.objects.get(indicador=indicador, estado=True)
			except SistemaIntegradoGestion.DoesNotExist:
				sistema_integrado_gestion = SistemaIntegradoGestion()
				pass

			sistema_integrado_gestion.indicador = indicador
			sistema_integrado_gestion.periodo = request.POST['periodo']
			sistema_integrado_gestion.save()

			if (sistema_integrado_gestion.itemSIG.count() > 0):
				sistema_integrado_gestion.itemSIG.all().delete()
			for s in sistemas:
				dicc = json.loads(s)
				val_anio = int(dicc['anio'])
				val_periodo_numero = int(dicc['periodo_numero'])
				val_valor_inicial = float(dicc['valor_inicial'])
				val_valor_esperado = float(dicc['valor_esperado'])
				# print("P: %s A: %s VI: %s VE: %s" % (val_periodo_numero, val_anio, val_valor, val_tipo_valor))
				if(val_valor_inicial > 0 or val_valor_esperado > 0 and val_anio > 1900 and val_anio < 2500):
					item = ItemSistemaIntegradoGestion()
					item.anio = val_anio
					item.periodo_numero = val_periodo_numero
					item.valor_inicial = val_valor_inicial
					item.valor_esperado = val_valor_esperado
					item.save()
					sistema_integrado_gestion.itemSIG.add(item)
					sistema_integrado_gestion.save()

			respuesta['mensaje'] = "Se almaceno sistema integrado de gestion correctamente"
			return HttpResponse(json.dumps(respuesta))
		else:
			return HttpResponse("peticion invalida, not ajax", status=403)


	def get(self, request):
		if self.VER_PROGRAMACION in request.GET:
			return self.ver_informacion_base(request)

		return HttpResponse("peticion invalida", status=403)


	def post(self, request):
		if self.AGREGAR_FUENTE_FINANCIACION in request.GET:
			return self.agregar_fuente_financiacion_ajax(request)

		if self.AGREGAR_SISTEMA_INTEGRADO_GESTION in request.GET:
			return self.agregar_sistema_integrado_gestion(request)

		return HttpResponse("peticion invalida", status=403)