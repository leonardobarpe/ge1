from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse, render
from django.template import RequestContext


# Create your views here.
# --------------------------------------------------------------------------- Logueo
def inicioSesion(request):
#	front1 = request.user.has_module_perms('front1')
#	tableroMando = request.user.has_module_perms('tableroMando')
	return render_to_response('inicioSesion.html', locals())
# --------------------------------------------------------------------------- Inicio
def inicio(request):
	return render_to_response('inicio.html', locals())