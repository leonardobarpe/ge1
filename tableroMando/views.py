from django.shortcuts import render
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse, render
from django.template import RequestContext
from django.contrib.auth.models import User
from datetime import datetime, date, timedelta
from django.urls import reverse
from django.views.generic import View
from tableroMando.forms import *


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

	ACCION_LISTAR = 'listar_i'
	TEMPLATE_LISTAR = 'listar_indicadores.html'

	ACCION_ELIMINAR = 'eliminar'


	def agregar_indicador(self, request):
		formulario = IndicadorFormulario(request.POST or None)
		abrebiatura_indicadores = Indicador.ABREBIATURA_INDICADORES

		indicador = None
		if 'indicador' in request.GET:
			indicador = Indicador.objects.get(pk=request.GET['indicador'])

		form_medicion = MedicionForm(request.POST or None)

		try:
			medicion = Medicion.objects.get(indicador=indicador)
		except Medicion.DoesNotExist:
			medicion = None
			pass

		if formulario.is_valid():
			if not indicador:
				nuevo_i = formulario.save(commit=False)
				# nuevo_i.usuario_registro = User.objects.get(pk=request.user.id)
				nuevo_i.save()
				return HttpResponseRedirect('/tablero-Mando/indicador/?agregar&indicador=%s' % nuevo_i.pk)
			else:
				indicador.tipo = formulario.cleaned_data.get('tipo')
				# indicador.prefijo = formulario.cleaned_data.get('prefijo')
				indicador.consecutivo = formulario.cleaned_data.get('consecutivo')
				indicador.nombre_identificador = formulario.cleaned_data.get('nombre_identificador')
				indicador.objetivo = formulario.cleaned_data.get('objetivo')
				indicador.producto_mide = formulario.cleaned_data.get('producto_mide')
				indicador.tipo_medicion = formulario.cleaned_data.get('tipo_medicion')
				indicador.ciclo = formulario.cleaned_data.get('ciclo')
				indicador.periodicidad = formulario.cleaned_data.get('periodicidad')
				indicador.ambito = formulario.cleaned_data.get('ambito')
				indicador.dimension = formulario.cleaned_data.get('dimension')
				# indicador.version = formulario.cleaned_data.get('version')
				indicador.responsable = formulario.cleaned_data.get('responsable')
				indicador.normatividad = formulario.cleaned_data.get('normatividad')
				indicador.limite_reporte = formulario.cleaned_data.get('limite_reporte')
				indicador.recurrencia = formulario.cleaned_data.get('recurrencia')
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


	def listar_indicadores(self, request):
		indicadores = Indicador.objects.filter(estado=True)
		return render(request, self.TEMPLATE_LISTAR, locals())


	def eliminar_indicador(self, request):
		indicador = Indicador.objects.get(pk=request.GET['indicador'])
		indicador.estado = False
		indicador.save()
		return HttpResponseRedirect('/tablero-Mando/indicador/?listar_i')


	def get(self, request):
		if self.ACCION_AGREGAR in request.GET:
			return self.agregar_indicador(request)

		if self.ACCION_LISTAR in request.GET:
			return self.listar_indicadores(request)

		if self.ACCION_ELIMINAR in request.GET:
			return self.eliminar_indicador(request)

		return HttpResponse("peticion invalida", status=403)


	def post(self, request):
		if self.ACCION_AGREGAR in request.GET:
			return self.agregar_indicador(request)

		if self.ACCION_AGREGAR_MEDICION in request.GET:
			return self.agregar_medicion(request)

		return HttpResponse("peticion invalida", status=403)


