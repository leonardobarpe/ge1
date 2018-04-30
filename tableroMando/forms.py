from django import forms
from .models import Indicador, Medicion


class IndicadorFormulario(forms.ModelForm):
	class Meta:
		model = Indicador
		exclude = (
			'fecha_creacion',
			'fecha_modificacion',
			'rango_inicial',
			'rango_final'
			# 'usuario_registro',
			)
		fields = (
			'tipo',
			'consecutivo',
			'nombre_identificador',
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


		