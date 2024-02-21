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

from mf.crud.forms import TeamForm, CategoryForm
from mf.crud.models import Team, Category, Tournament, DetTournament, Ridding, Confrontations
from mf.crud.functions import *

import os
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from django.conf import settings
from datetime import date

import random

class TeamListView(LoginRequiredMixin, ValidatePermissionMixin, TemplateView):
    template_name = 'team/list.html'
    permission_required = 'view_team'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        db = 'default'
        try:
            sede = request.POST['sede']
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Team.objects.using(db).all():
                    data.append(i.toJSON())           
            elif action == 'add':
                perms = ['add_team']
                group = request.user.groups.first()
                authorized = ValidatePermissions(perms, group)
                if(authorized == False):
                    data['error'] = 'Disculpe, usted no tiene permisos para ejecutar esta acción'
                elif(authorized == True):
                    with transaction.atomic():
                        tm = Team()
                        tm.name = request.POST['name']
                        tm.dni = request.POST['dni']
                        tm.birthdate = request.POST['birthdate']
                        tm.gender = request.POST['gender']
                        tm.email = request.POST['email']
                        tm.category_id = request.POST['category']
                        if request.FILES:
                            tm.logo = request.FILES['logo']
                        tm.save()
            elif action == 'addCategory':
                perms = ['add_category']
                group = request.user.groups.first()
                authorized = ValidatePermissions(perms, group)
                if(authorized == False):
                    data['error'] = 'Disculpe, usted no tiene permisos para ejecutar esta acción'
                elif(authorized == True):
                    ctg = Category()
                    ctg.name = request.POST['name']
                    ctg.description = request.POST['description']
                    ctg.save()
            elif action == 'edit':
                perms = ['change_team']
                group = request.user.groups.first()
                authorized = ValidatePermissions(perms, group)
                if(authorized == False):
                    data['error'] = 'Disculpe, usted no tiene permisos para ejecutar esta acción'
                elif(authorized == True):                       
                    tm = Team.objects.using(db).get(pk=request.POST['id'])
                    tm.name = request.POST['name']
                    tm.dni = request.POST['dni']
                    tm.birthdate = request.POST['birthdate']
                    tm.gender = request.POST['gender']
                    tm.email = request.POST['email']
                    tm.category_id = request.POST['category']
                    if request.FILES:
                        tmc.logo = request.FILES['logo']
                    tm.save()
            elif action == 'delete':
                perms = ['delete_team']
                group = request.user.groups.first()
                authorized = ValidatePermissions(perms, group)
                if(authorized == False):
                    data['error'] = 'Disculpe, usted no tiene permisos para ejecutar esta acción'
                elif(authorized == True):
                    team = Team.objects.using(db).get(pk=request.POST['id']).delete()
            else:
                data['error'] = "Ha ocurrido un error"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Participantes'
        context['form'] = TeamForm()
        context['formCategory'] = CategoryForm()
        context['data'] = getCompanyData()
        context['today'] = date.today()
        context['events'] = get_events_today()
        context['q_events'] = get_q_events_today()
        return context