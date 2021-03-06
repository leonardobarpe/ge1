from django import forms
from .models import Indicador, Medicion, Armonizacion


class IndicadorFormulario(forms.ModelForm):
	class Meta:
		model = Indicador
		exclude = (
			'fecha_creacion',
			'fecha_modificacion',
			'rango_inicial',
			'rango_final',
			# 'tipo',
			# 'usuario_registro',
			)
		fields = (
			'tipo_indicador',
			'consecutivo',
			'nombre_indicador',
			'objetivo',
			'producto_mide',
			'tipo_medicion',
			'ciclo',
			'periodicidad',
			'ambito',
			'dimension',
			'responsable',
			'fecha_actualizacion', # fecha que actualiza el indicador
			'normatividad',
			'limite_reporte',
			'version',
			'recurrencia',
			)
		widgets = {
            'normatividad': forms.SelectMultiple(attrs={'class': 'form-control','multiple':'','data-placeholder':'Seleccione algunas opciones'}),
            'tipo_indicador': forms.SelectMultiple(attrs={'class': 'form-control','multiple':'','data-placeholder':'Seleccione algunas opciones'}),
        }

	# Constructor que asigna form-control a todos los elemtos del formulario
	def __init__(self, *args, **kwargs):
		super(IndicadorFormulario, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

		self.fields['objetivo'].widget.attrs['rows']= 2
		self.fields['producto_mide'].widget.attrs['rows']= 2
		self.fields['fecha_actualizacion'].required = False
		
		# Desactivar fields
		self.fields['version'].required = False
		self.fields['tipo_medicion'].required = False
		self.fields['recurrencia'].required = False
		self.fields['version'].widget.attrs['disabled'] = 'disabled'
		self.fields['tipo_medicion'].widget.attrs['disabled'] = 'disabled'
		self.fields['recurrencia'].widget.attrs['disabled'] = 'disabled'



class MedicionForm(forms.ModelForm):
	class Meta:
		model = Medicion
		exclude = ('indicador',)
		fields = (
			'tipo_formula',
			'unidad_medicion',
			'tendencia',
			'archivo_asociado',
			'nombre_variable_1',
			'nomenclaruta_1',
			'unidad_1',
			'fuente_1',
			
			'nombre_variable_2',
			'nomenclaruta_2',
			'unidad_2',
			'fuente_2',

			'nombre_respuesta',
			'nomenclaruta_respuesta',
			'unidad_respuesta',
			'fuente_respuesta',

			'formula',
			'interpretacion_resultado',
			'rango_inicial',
			'rango_final',
			'responsable_reporte',
			'responsable_consolidacion',
			'responsable_analisis_seguimiento',
			'responsable_decisiones',
		)

	def __init__(self, *args, **kwargs):
		super(MedicionForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
		self.fields['interpretacion_resultado'].widget.attrs['rows']= 3
		self.fields['formula'].widget.attrs['rows']= 2


class ArmonizacionForm(forms.ModelForm):
	class Meta:
		model = Armonizacion
		exclude = ('indicador',)
		fields = (
			'linea',
			'meta',
			'tipo_proceso',
			'proceso',
			'programa',
			'subprograma',
			'subproceso',
			'tipo_armonizacion',
			)
		widgets = {
            'tipo_armonizacion': forms.SelectMultiple(attrs={'multiple':''}),
        }

	def  __init__(self, *args, **kwargs):
		super(ArmonizacionForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control select-chossen'


class FiltrosIndicadoresForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super(FiltrosIndicadoresForm, self).__init__(*args, **kwargs)
		# formulario
		self.fields['codigo_indicador'] = forms.IntegerField(required=False)
		choices_n = [(0, 'Ninguno'),]
		choices_n.extend([(i.id, i.nombre_indicador.nombre) for i in Indicador.objects.filter(estado=True)])
		self.fields['nombre_indicador'] = forms.ChoiceField(choices=choices_n, required=False)

		choices_t = [(0, 'Ninguno'),]
		choices_t.extend(Indicador.TIPO_INDICADOR_OPCIONES)
		self.fields['tipo_proceso'] = forms.ChoiceField(choices=choices_t, required=False)

		choices_c = [(0, 'Ninguno'),]
		choices_c.extend(Indicador.CICLO_OPCIONES)
		self.fields['ciclo'] = forms.ChoiceField(choices=choices_c, required=False)
		
		#atributos
		self.fields['codigo_indicador'].widget.attrs['class'] = 'col-sm-7 form-control form-control-sm'
		self.fields['codigo_indicador'].widget.attrs['placeholder'] ='Digita el código'
		self.fields['nombre_indicador'].widget.attrs['class'] = 'col-sm-7 form-control form-control-sm'
		self.fields['tipo_proceso'].widget.attrs['class'] = 'col-sm-7 form-control form-control-sm'
		self.fields['ciclo'].widget.attrs['class'] = 'col-sm-8 form-control form-control-sm'
