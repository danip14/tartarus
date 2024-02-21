from django.urls import path
from mf.crud.views.dashboard.views import *
from mf.crud.views.companyInfo.views import *
from mf.crud.views.events.views import *
from mf.crud.views.category.views import *
from mf.crud.views.team.views import *
from mf.crud.views.player.views import *
from mf.crud.views.dettournament.views import *
from mf.crud.views.tournament.views import * 

app_name = 'crud'

urlpatterns = [
    # Dashboard
    path('inicio/', DashboardView.as_view(), name='dashboard'),
    # Company Info
    path('informacion/', CompanyInfoView.as_view(), name='companyinfo'),
    # Calendar
    path('eventos/list/', EventosListView.as_view(), name='events'),
    # NEW URLS
    # Category
    path('categorias/list/', CategoryListView.as_view(), name='category_list'),
    # Teams
    path('teams/list/', TeamListView.as_view(), name='team_list'),
    # Tournaments
    path('torneos/list/', TournamentListView.as_view(), name='tornauments'),
    # Dettournament
    path('torneos/list/<int:idTournament>/<int:roundNumber>/', DetTournamentistView.as_view(), name='tornauments_list'),
    # Players
    path('jugadores/', PlayerView.as_view(), name='player')
]