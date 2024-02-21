from django.forms import *
from datetime import datetime
from mf.crud.models import *

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
 
class PermisologyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Permisology
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control UpperCase',
                    'placeholder': 'Título',
                    'autocomplete': 'off'
                }
            ),
            'description':Textarea(
                attrs={
                    'placeholder': 'Descripción del Permiso ó Evento',
                    'class': 'form-control',
                    'rows': 3,
                    'autocomplete': 'off'
                }
            ),
            'day': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'placeholder': 'YYYY-MM-DD',
                    'id': 'day',
                    'data-target': '#day',
                    'data-toggle': 'datetimepicker'
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class CompanyInfoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = CompanyInfo
        fields = '__all__'
        widgets = {
            'name':TextInput(
                attrs={
                    'placeholder': 'Razón social',
                    'class': 'form-control UpperCase',
                    'autocomplete': 'off',
                    'disabled': 'disabled',
                }
            ),
            'comercialName':TextInput(
                attrs={
                    'placeholder': 'Nombre Comercial',
                    'class': 'form-control UpperCase',
                    'autocomplete': 'off',
                    'disabled': 'disabled',
                }
            ),
            'nit':TextInput(
                attrs={
                    'placeholder': 'NIT de la empresa',
                    'class': 'form-control UpperCase',
                    'autocomplete': 'off',
                    'disabled': 'disabled',
                }
            ),
            'address':TextInput(
                attrs={
                    'placeholder': 'Ubicación de la sede',
                    'class': 'form-control UpperCase',
                    'autocomplete': 'off',
                    'disabled': 'disabled',
                }
            ),
            'city':TextInput(
                attrs={
                    'placeholder': 'Ciudad',
                    'class': 'form-control UpperCase',
                    'autocomplete': 'off',
                    'disabled': 'disabled',
                }
            ),
            'phone':TextInput(
                attrs={
                    'placeholder': 'Números de contacto',
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'disabled': 'disabled',
                }
            ),
            'email':TextInput(
                attrs={
                    'placeholder': 'Dirección de correo electronico',
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'disabled': 'disabled',
                }
            ),
            'services': Textarea(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Indique los detalles de servicios y productos que ofrece la empresa...',
                    'rows': 4,
                    'disabled': 'disabled',
                }
            ),
            'logo': FileInput(
                attrs={
                    'class': 'form-control',
                    'disabled': 'disabled',
                }
            ),

        }
        
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class EventosForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Eventos
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control UpperCase',
                    'placeholder': 'Título',
                    'autocomplete': 'off'
                }
            ),
            'description':Textarea(
                attrs={
                    'placeholder': 'Descripción del evento',
                    'class': 'form-control',
                    'rows': 3,
                    'autocomplete': 'off'
                }
            ),
            'day': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'placeholder': 'YYYY-MM-DD',
                    'id': 'day',
                    'type': 'date',
                    'data-target': '#day',
                    'data-toggle': 'datetimepicker'
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Nombre de la categoría',
                    'class': 'form-control UpperCase',
                    'autocomplete': 'off'
                }
            ),
            'description': Textarea(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Descripción de la categoría',
                    'rows': 2,
                }
            ),
        }
        exclude = ['user_updated', 'user_creation', 'status']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class TeamForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Team
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Nombre del participante',
                    'class': 'form-control UpperCase',
                    'autocomplete': 'off'
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder': 'Ejemplo: V-00000000',
                    'class': 'form-control UpperCase',
                    'autocomplete': 'off'
                }
            ),
             'birthdate': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'datejoined',
                    'data-target': '#datejoined',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'gender': Select(
                attrs={
                    'autofocus': True,
                    'class': 'form-control medium',
            }),
            'email': TextInput(
                attrs={
                    'placeholder': 'example@dominio.com',
                    'type': 'email',
                    'class': 'form-control UpperCase',
                    'autocomplete': 'off'
                }
            ),
            'category': Select(
                attrs={
                    'autofocus': True,
                    'class': 'form-control medium',
            }),
            'logo': FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
        exclude = ['status', 'logo']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class PlayerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['team'].widget.attrs['autofocus'] = True

    class Meta:
        model = Player
        fields = '__all__'
        widgets = {
            'team': Select(
                attrs={
                    'autofocus': True,
                    'class': 'form-control medium',
            }),
            'name': TextInput(
                attrs={
                    'placeholder': 'Nombre del jugador',
                    'class': 'form-control UpperCase',
                    'autocomplete': 'off'
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class TournamentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['datejoined'].widget.attrs['autofocus'] = True

    class Meta:
        model = Tournament
        fields = '__all__'
        widgets = {
            'datejoined': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'datejoined',
                    'data-target': '#datejoined',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'name': TextInput(
                attrs={
                    'placeholder': 'Nombre del torneo',
                    'class': 'form-control UpperCase',
                    'autocomplete': 'off'
                }
            ),
            'category': Select(
                attrs={
                    'autofocus': True,
                    'class': 'form-control medium',
            }),
            'qtyLosses':NumberInput(
                attrs={
                    'placeholder': 'Perdidas',
                    'class': 'form-control text-center',
                    'onclick': 'this.select()',
                    'autocomplete': 'off',
                    'min': 0,
                    'step': 1,
                    'value': 0,
                }
            ),
        }
        exclude = ['status', 'cantidad']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data