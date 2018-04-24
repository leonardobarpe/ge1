from django import forms
from .models import Indicador, Medicion

# class IndicadorFormulario(forms.ModelForm):
# 	class Meta:
# 		model = Indicador
# 		fields = [
# 			'tipo',
# 			'nombre',
# 			'nomenclador',
# 			'ciclo',
# 			'fechaCreacion',
# 			'version',
# 			'prefijo',
# 			'objetivo',
# 			'periodicidad',
# 			'responsable',
# 			'fechaActualiza',
# 			'consecutivo',
# 			'productoMide',
# 			'ambito',
# 			'normaApli',
# 		]
# 	# Constructor que asigna form-control a todos los elemtos del formulario
# 	def __init__(self, *args, **kwargs):
# 		super(IndicadorFormulario, self).__init__(*args, **kwargs)
# 		for visible in self.visible_fields():
# 			visible.field.widget.attrs['class'] = 'form-control'
# 		self.fields['fechaCreacion'].widget.attrs['readonly']= True
# 		self.fields['version'].widget.attrs['readonly']= True
# 		self.fields['prefijo'].widget.attrs['readonly']= True
# 		self.fields['objetivo'].widget.attrs['rows']= 2
# 		self.fields['productoMide'].widget.attrs['rows']= 2

class IndicadorFormulario(forms.ModelForm):
	class Meta:
		model = Indicador
		exclude = (
			'fecha_creacion',
			'fecha_actualizacion',
			# 'usuario_registro',
			'rango_inicial',
			'rango_final'
			)
		fields = (
			'tipo',
			'prefijo',
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
			'normatividad',
			'limite_reporte',
			'version',
			'recurrencia',
			)
		widgets = {
            'normatividad': forms.SelectMultiple(attrs={'class': 'form-control','multiple':''}),
        }

	# Constructor que asigna form-control a todos los elemtos del formulario
	def __init__(self, *args, **kwargs):
		super(IndicadorFormulario, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
		self.fields['version'].widget.attrs['readonly']= True
		self.fields['prefijo'].widget.attrs['readonly']= True
		self.fields['tipo_medicion'].widget.attrs['readonly']= True
		self.fields['recurrencia'].widget.attrs['readonly']= True
		# self.fields['tipo_medicion'].widget.attrs['disabled'] = 'disabled'
		# self.fields['recurrencia'].widget.attrs['disabled'] = 'disabled'
		self.fields['objetivo'].widget.attrs['rows']= 2
		self.fields['producto_mide'].widget.attrs['rows']= 2



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
		self.fields['interpretacion_resultado'].widget.attrs['rows']= 2
		self.fields['formula'].widget.attrs['rows']= 2


# ------------------------------------------

# class IndicadorForm(forms.ModelForm):
# 	class Meta:
# 		model = Indicador
# 		fields = ('consecutivo', 'nombre',)


			

		