## Esta es la tabla de registro de equipos
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpRequest
from django.views.generic import TemplateView, ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db import transaction
import json
from decimal import Decimal
from django.db.models import IntegerField
from django.db.models.functions import Cast

from mf.crud.mixins import IsSuperuserMixin, ValidatePermissionMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from mf.crud.forms import TournamentForm
from mf.crud.models import Tournament, Confrontations, Team, DetTournament, Ridding
from mf.crud.functions import *

import os
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from django.conf import settings
from datetime import date

class TournamentListView(LoginRequiredMixin, ValidatePermissionMixin, TemplateView):
    template_name = 'tournament/list.html'
    permission_required = 'view_tournament'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        db = 'default'
        try:
            sede = 'NA'
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Tournament.objects.all().exclude(status=4):
                    item = i.toJSON()
                    item['lastRound'] = 0
                    lastRound = Confrontations.objects.filter(tournament__id=i.id).order_by('-id')[:1]
                    for i in lastRound:
                        item['lastRound'] = i.roundNumber
                    data.append(item)
            elif action == 'getTeams':
                data = []
                number = 0
                for i in Team.objects.filter(category__id=request.POST['category']).order_by('name'):
                    number += 1
                    team = {
                        'number': number,
                        'id': i.id,
                        'name': i.name
                    }
                    data.append(team)
            elif action == 'addTeams':
                teams = json.loads(request.POST['teams'])
                tournamentId = request.POST['tournamentId']
                
                with transaction.atomic():
                    for i in teams:
                        det = DetTournament()
                        det.tournament_id = tournamentId
                        det.team_id = i
                        det.earned = 0
                        det.losses = 0
                        det.tied = 0
                        det.removed = 0
                        det.save()

                        r = Ridding()
                        r.tournament_id = tournamentId
                        r.team_id = i
                        r.roundNumber = 0
                        r.free = 0
                        r.save()

                    t = Tournament.objects.get(pk=tournamentId)
                    t.status = 1
                    t.save()
            elif action == 'add':
                perms = ['add_tournament']
                group = request.user.groups.first()
                authorized = ValidatePermissions(perms, group)
                if(authorized == False):
                    data['error'] = 'Disculpe, usted no tiene permisos para ejecutar esta acción'
                elif(authorized == True):
                    with transaction.atomic():
                        t = Tournament()
                        t.name = request.POST['name']
                        t.datejoined = request.POST['datejoined']
                        t.category_id = request.POST['category']
                        t.qtyLosses = request.POST['qtyLosses']
                        t.status = 0
                        t.save()    
            elif action == 'edit':
                perms = ['change_tournament']
                group = request.user.groups.first()
                authorized = ValidatePermissions(perms, group)
                if(authorized == False):
                    data['error'] = 'Disculpe, usted no tiene permisos para ejecutar esta acción'
                elif(authorized == True):                       
                    t = Tournament.objects.get(pk=request.POST['id'])
                    t.name = request.POST['name']
                    t.datejoined = request.POST['datejoined']
                    t.category_id = request.POST['category']
                    t.qtyLosses = request.POST['qtyLosses']
                    t.save() 
            elif action == 'delete':
                perms = ['delete_tournament']
                group = request.user.groups.first()
                authorized = ValidatePermissions(perms, group)
                if(authorized == False):
                    data['error'] = 'Disculpe, usted no tiene permisos para ejecutar esta acción'
                elif(authorized == True):
                    t = Tournament.objects.get(pk=request.POST['id'])
                    t.status = 4
                    t.save()
            else:
                data['error'] = "Ha ocurrido un error"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Torneos'
        context['form'] = TournamentForm()
        context['data'] = getCompanyData()
        context['today'] = date.today()
        context['events'] = get_events_today()
        context['q_events'] = get_q_events_today()
        return context