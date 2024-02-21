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
from mf.crud.models import Team, Category, Confrontations, DetConfrontations, DetTournament, Ridding, Tournament
from mf.crud.functions import *

import os
import random
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from django.conf import settings
from datetime import date

class DetTournamentistView(LoginRequiredMixin, TemplateView):
    template_name = 'dettournament/list.html'
    permission_required = 'view_team'

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
                for i in Team.objects.using(db).all():
                    data.append(i.toJSON())
            elif action == 'RecordResults':
                tournament = self.kwargs['idTournament']
                teams = json.loads(request.POST['teams'])
                roundNumber = self.kwargs['roundNumber']

                for i in teams:
                    idTeam1 = i[0]
                    idTeam2 = i[2]
                    qtyTeam1 = i[1]
                    qtyTeam2 = i[3]

                    gain1 = 0
                    gain2 = 0
                    losses1 = 0
                    losses2 = 0
                    point1 = 1
                    point2 = 1
                    tied1 = 1
                    tied2 = 1

                    if qtyTeam1 != qtyTeam2:
                        tied1 = 0
                        tied2 = 0

                        if qtyTeam1 > qtyTeam2:
                            gain1 = 1
                            losses1 = 0
                            point1 = 3

                            gain2 = 0
                            losses2 = 1
                            point2 = 0
                        else:
                            gain2 = 1
                            losses2 = 0
                            point2 = 3

                            gain1 = 0
                            losses1 = 1
                            point1 = 0

                    with transaction.atomic():
                        team1 = DetTournament.objects.get(tournament__id=tournament, team__id=idTeam1)
                        team1.plays += 1
                        team1.earned += gain1
                        team1.losses += losses1
                        team1.tied += tied1
                        team1.points += point1
                        team1.lastOpponent_id = idTeam2
                        team1.save()

                        team2 = DetTournament.objects.get(tournament__id=tournament, team__id=idTeam2)
                        team2.plays += 1
                        team2.earned += gain2
                        team2.losses += losses2
                        team2.tied += tied2
                        team2.points += point2
                        team2.lastOpponent_id = idTeam1
                        team2.save()

                        confrontation1 = Confrontations.objects.get(tournament__id=tournament, roundNumber=roundNumber, team1__id=idTeam1)
                        confrontation1.status = 2
                        confrontation1.qtyRound1 += qtyTeam1
                        confrontation1.save()

                        confrontation2 = Confrontations.objects.get(tournament__id=tournament, roundNumber=roundNumber, team2__id=idTeam2)
                        confrontation2.status = 2
                        confrontation2.qtyRound2 += qtyTeam2
                        confrontation2.save()
                        
                        tr = Tournament.objects.get(pk=tournament)
                        maxLosses = int(tr.qtyLosses)
                        for i in DetTournament.objects.filter(tournament__id=tournament):
                            if i.losses == maxLosses:
                                free = Ridding.objects.get(tournament__id=tournament, team__id=i.team.id)
                                free.status = 0
                                free.save()
            elif action == 'GenerateNewRound':
                TournamentId = self.kwargs['idTournament']
                roundNumber = pk=self.kwargs['roundNumber']

                t = Tournament.objects.get(pk=TournamentId)
                maxLosses = int(t.qtyLosses)

                roundNumber += 1

                # Obtenemos los equipos
                teams = []
                for i in DetTournament.objects.filter(tournament__id=TournamentId).exclude(losses=maxLosses).order_by('losses'):
                    teams.append(i.team.id)

                if len(teams) == 1:
                    tm = Tournament.objects.get(pk=TournamentId)
                    tm.status = 3
                    tm.save()
                    data['error'] = 'El torneo ha finalizado. No existen más combinaciones posibles' 

                else:

                    # Guardamos la cantidad de equipos
                    numberTeams = len(teams)

                    # Variable para guardar el equipo que libra
                    teamFreeing = 0

                    # Validamos que sea divisible entre 2
                    if numberTeams % 2 == 0:
                        pass
                    else:
                        freeTeams = []
                        for i in Ridding.objects.filter(tournament__id=TournamentId, free=0, status=1):
                            freeTeams.append(i.team.id)

                        if len(freeTeams) == 0:
                            Ridding.objects.filter(tournament__id=TournamentId).update(free=0)
                            for i in Ridding.objects.filter(tournament__id=TournamentId, free=0, status=1):
                                freeTeams.append(i.team.id)

                        for i in range(1):
                            teamFreeing = random.choice(freeTeams)

                        with transaction.atomic():
                            Ridding.objects.filter(tournament__id=TournamentId, team__id=teamFreeing).update(roundNumber=roundNumber, free=1)

                        if teamFreeing in teams:
                            teams.remove(teamFreeing)
        
                    # Reiniciamos el contador
                    numberTeams = len(teams)

                    if roundNumber == 1:
                        while numberTeams > 0:
                            confrontation = random.sample(teams, 2)
                            with transaction.atomic():
                                c = Confrontations()
                                c.tournament_id = TournamentId
                                c.team1_id = confrontation[0]
                                c.team2_id = confrontation[1]
                                c.roundNumber = roundNumber
                                c.save()

                                for i in confrontation:
                                    teams.remove(i)
                                    
                                numberTeams = len(teams)
                    else:
                        previousRoundNumber = roundNumber - 1
                        teamsDetails = []
                        previousConfrontaions = []

                        for i in teams:
                            detTeam = DetTournament.objects.filter(tournament__id=TournamentId, team__id=i)[:1].get()
                            teamsDetails.append([i, detTeam.losses, detTeam.lastOpponent_id])
                            previousConfrontaions.append([i, detTeam.lastOpponent_id])
                            previousConfrontaions.append([detTeam.lastOpponent_id, i])

                        try:
                            retries = 0
                            duplicate = True

                            while duplicate == True and retries < 10:
                                retries += 1
                                newConfrontations = self.generateTeams(teamsDetails)

                                i = 0
                                duplicate = False
                                while duplicate == False and i < len(newConfrontations):
                                    if newConfrontations[i] in previousConfrontaions:
                                        duplicate = True
                                    i+=1

                            with transaction.atomic():
                                for i in newConfrontations:
                                    c = Confrontations()
                                    c.tournament_id = TournamentId
                                    c.team1_id = i[0]
                                    c.team2_id = i[1]
                                    c.roundNumber = roundNumber
                                    c.save()
                        except:
                            data['error'] = "Ourrió un error. Por favor, vuelve a intentar."
                    
                    data = {
                        'id': TournamentId,
                        'round': roundNumber,
                    }
            
                    t.status = 2
                    t.save()
            else:
                data['error'] = "Ha ocurrido un error"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def generateTeams(self, teamsDetails):
        newConfrontations = []
        allTeams = teamsDetails.copy()

        x = 0
        temp = []
        tempFree = []
        byDelete = []
        qtyLosses = 0
        while len(allTeams) > 0:
            if int(allTeams[x][1]) == int(qtyLosses):
                temp.append(allTeams[x])
                byDelete.append(allTeams[x]) 
            if allTeams[x][1] != qtyLosses or allTeams.index(allTeams[x]) == (len(allTeams) - 1):
                x = 0
                qtyLosses += 1
                if len(temp) != 0:
                    if len(temp) == 1:
                        tempFree.append(temp[0])
                        byDelete.append(temp[0])
                        temp = []

                    if len(temp) % 2 != 0:
                        for i in range(1):
                            free = random.choice(temp)
                            tempFree.append(free)
                            byDelete.append(free)
                            if free in temp:
                                temp.remove(free)
                    
                    retries = 0
                    previous = []
                    temp2 = temp.copy()
                    maxFifty = False
                    while len(temp) > 0:
                        for a in range(1):
                            i = random.choice(temp)
                            for b in range(1):
                                g = random.choice(temp)
                                if i[0] != g[0] and g[0] != i[2] and i[0] != g[2]:
                                    previous.append([i[0], g[0]])
                                    if i in temp:
                                        temp.remove(i)
                                    if g in temp:
                                        temp.remove(g)
                                else:
                                    retries += 1

                                if retries > 50 and maxFifty == False:
                                    maxFifty = True
                                    temp = temp2.copy()
                                    previous = []
                                    retries = 0

                                if retries > 50 and maxFifty == True:
                                    if len(temp) != 0:
                                        if i not in tempFree:
                                            tempFree.append(i)
                                        if g not in tempFree:
                                            tempFree.append(g)
                                        if i in temp:
                                            temp.remove(i)
                                        if g in temp:
                                            temp.remove(g)
                    for i in previous:
                        newConfrontations.append(i)
                    
                    for i in temp2:
                        byDelete.append(i)
                    
                    for i in byDelete:
                        if i in allTeams:
                            allTeams.remove(i)

                    byDelete = []
            else:
                x += 1

        while len(tempFree) > 0:
            for a in range(1):
                i = random.choice(tempFree)
                for b in range(1):
                    g = random.choice(tempFree)
                    if i[0] != g[0]:
                        newConfrontations.append([i[0], g[0]])
                        if i in tempFree:
                            tempFree.remove(i)
                        if g in tempFree:
                            tempFree.remove(g)

        return newConfrontations

    def getDetTournament(self, idTournament, roundNumber):
        detailsTournament = []
        for i in DetTournament.objects.filter(tournament__id=idTournament).order_by('-points'):
            detailsTournament.append(i.toJSON())
        return detailsTournament

    def getConfrontations(self, idTournament, roundNumber):
        teamsConfrontations = []
        for i in Confrontations.objects.filter(tournament__id=idTournament, roundNumber=roundNumber):
            item = i.toJSON()
            if i.qtyRound1 == i.qtyRound2:
                item['color1'] = 'bg-success'
                item['color2'] = 'bg-success'
            elif i.qtyRound1 > i.qtyRound2:
                item['color1'] = 'bg-success'
                item['color2'] = 'bg-secondary'
            else:
                item['color1'] = 'bg-secondary'
                item['color2'] = 'bg-success'
            teamsConfrontations.append(item)
        return teamsConfrontations

    def getFreeTeams(self, idTournament, roundNumber):
        freeTeams = []
        for i in Ridding.objects.filter(tournament__id=idTournament, roundNumber=roundNumber, status=1, free=1):
            freeTeams.append(i.toJSON())
        return freeTeams

    def getStatusConfrontations(self, idTournament, roundNumber):
        status = 0
        confrontation = Confrontations.objects.filter(tournament__id=idTournament, roundNumber=roundNumber)[:1]
        for i in confrontation:
            status = i.status

        if status == 2:
            status = 'disabled'
        else:
            status = ''

        return status

    def getRounds(self, idTournament):
        lastRound = 0
        rounds = []
        c = Confrontations.objects.filter(tournament__id=idTournament).order_by('-id')[:1]
        for i in c:
            lastRound = i.roundNumber

        count = 0
        while count < lastRound:
            count += 1
            rounds.append(count)
        return rounds

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Equipos'
        context['form'] = TeamForm()
        context['formCategory'] = CategoryForm()
        context['data'] = getCompanyData()
        context['today'] = date.today()
        context['events'] = get_events_today()
        context['q_events'] = get_q_events_today()
        context['torneos'] = self.getConfrontations(self.kwargs['idTournament'], self.kwargs['roundNumber'])
        context['detallesTorneos'] = self.getDetTournament(self.kwargs['idTournament'], self.kwargs['roundNumber'])
        context['statusTorneo'] = self.getStatusConfrontations(self.kwargs['idTournament'], self.kwargs['roundNumber'])
        context['librando'] = self.getFreeTeams(self.kwargs['idTournament'], self.kwargs['roundNumber'])
        context['rounds'] = self.getRounds(self.kwargs['idTournament'])
        context['rondaTorneo'] = self.kwargs['roundNumber']
        context['idTorneo'] = self.kwargs['idTournament']
        
        return context