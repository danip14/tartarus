from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib import request
from django.utils import timezone
from django.db import transaction
from config.settings import MEDIA_URL

from django.contrib.auth.mixins import LoginRequiredMixin
from mf.crud.mixins import IsSuperuserMixin, ValidatePermissionMixin

from datetime import date
from datetime import datetime, timedelta

from mf.crud.models import Tournament
from django.db.models.functions import Coalesce
from django.db.models import Sum

from mf.crud.functions import *

import os
from pathlib import Path

class DashboardView(LoginRequiredMixin, ValidatePermissionMixin, TemplateView):
    template_name = 'dashboard.html'
    permission_required = 'view_tournament'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            db = 'default'
            action = request.POST['action']
            if action == 'get_graph_sales':
                year = datetime.now().year
                for m in range(1, 13):
                    total = Tournament.objects.filter(datejoined__year=year, datejoined__month=m).aggregate(
                        r=Coalesce(Sum('cantidad'), 0)).get('r')
                data = {
                    'name': 'Porcentaje de Torneos',
                    'showInLegend': False,
                    'colorByPoint': True,
                    'data': self.get_graph_sales()
                }
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    
    def get_graph_sales(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1, 13):
                total = Tournament.objects.filter(datejoined__year=year, datejoined__month=m).aggregate(
                    r=Coalesce(Sum('cantidad'), 0)).get('r')
                data.append(float(total))
        except:
            pass
        return data

    def get_name_month(self):
        data = ''
        month = datetime.now().month
        if month == 1:
            data = 'Enero'
        elif month == 2:
            data = 'Febrero'
        elif month == 3:
            data = 'Marzo'
        elif month == 4:
            data = 'Abril'
        elif month == 5:
            data = 'Mayo'
        elif month == 6:
            data = 'Junio'
        elif month == 7:
            data = 'Julio'
        elif month == 8:
            data = 'Agosto'
        elif month == 9:
            data = 'Septiembre'
        elif month == 10:
            data = 'Octubre'
        elif month == 11:
            data = 'Noviembre'
        elif month == 12:
            data = 'Diciembre'
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'PRINCIPAL'
        context['today'] = date.today()
        context['month'] = self.get_name_month()
        context['year'] = datetime.now().year
        context['title_pag'] = 'Panel principal'
        context['title'] = 'INICIO'
        context['events'] = get_events_today()
        context['q_events'] = get_q_events_today()
        context['data'] = getCompanyData()
        return context
