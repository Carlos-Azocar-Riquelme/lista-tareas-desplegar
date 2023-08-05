from django import forms

#Modelos que necesitan validacion
from .models import Tarea

class TareaForm(forms.ModelForm):
  class Meta:
    model = Tarea
    exclude = []