from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.db import transaction

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from mf.crud.mixins import IsSuperuserMixin, ValidatePermissionMixin

from mf.crud.models import Player
from mf.crud.forms import PlayerForm
from mf.crud.functions import *

class PlayerView(LoginRequiredMixin, ValidatePermissionMixin, TemplateView):
    template_name = 'player/list.html'
    permission_required = 'view_player'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        db = 'default'
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Player.objects.using(db).all():
                    data.append(i.toJSON())
            elif action == 'add':
                perms = ['add_player',]
                group = request.user.groups.first()
                authorized = ValidatePermissions(perms, group)
                if(authorized == False):
                    data['error'] = 'Disculpe, usted no tiene permisos para ejecutar esta acción'
                elif(authorized == True):
                    with transaction.atomic():
                        p = Player()
                        p.name = request.POST['name']
                        p.team_id = request.POST['team']
                        p.save()
            elif action == 'edit':
                perms = ['change_player',]
                group = request.user.groups.first()
                authorized = ValidatePermissions(perms, group)
                if(authorized == False):
                    data['error'] = 'Disculpe, usted no tiene permisos para ejecutar esta acción'
                elif(authorized == True):
                    with transaction.atomic():
                        p = Player.objects.get(pk=request.POST['id'])
                        p.name = request.POST['name']
                        p.team_id = request.POST['team']
                        p.save()
            elif action == 'delete':
                perms = ['delete_player',]
                group = request.user.groups.first()
                authorized = ValidatePermissions(perms, group)
                if(authorized == False):
                    data['error'] = 'Disculpe, usted no tiene permisos para ejecutar esta acción'
                elif(authorized == True):
                    Player.objects.using('default').get(pk=request.POST['id']).delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Jugadores'
        context['list_url'] = reverse_lazy('crud:player')
        context['form'] = PlayerForm()
        context['data'] = getCompanyData()
        context['today'] = date.today()
        context['events'] = get_events_today()
        context['q_events'] = get_q_events_today()
        return context
