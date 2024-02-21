from django.core.files.storage import FileSystemStorage
from crum import get_current_user, get_current_request
from mf.user.models import User
from django.db import models
from datetime import datetime
from django.utils import timezone 
from datetime import date
from django.forms import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL
from mf.models import BaseModel
from django.utils.dateparse import parse_datetime
import pytz

IDENTITY_CHOICES = [
    ('V', 'V'),
    ('J', 'J'),
    ('E', 'E'),
    ('G', 'G'),
    ('FP', 'FP'),
]

SYMBOL_CHOICES = [
    ('Bs', 'Bs'),
    ('$', '$'),
]

STATUS_CHOICES = [
    ('ACTIVO', 'ACTIVO'),
    ('INACTIVO', 'INACTIVO'),
]

GENDER_CHOICES = [
    ('FEMENINO', 'FEMENINO'),
    ('MASCULINO', 'MASCULINO'),
]

class Permisology(models.Model):
    name = models.CharField(max_length=255, verbose_name='Permiso')
    description = models.CharField(max_length=255, verbose_name='Descripción')
    day = models.DateField(max_length=50, default=date.today().strftime('%Y-%m-%d'), verbose_name='Fecha de pago')
    color = models.CharField(max_length=250, default='#007bff', verbose_name='Color')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Permisos y Eventos'
        verbose_name_plural = 'Permisos y Eventos'
        ordering = ['id']

class CompanyInfo(models.Model):
    name = models.CharField(max_length=225, verbose_name="Razón Social")
    comercialName = models.CharField(max_length=225, verbose_name="Nombre Comercial")
    nit = models.CharField(max_length=225, verbose_name="NIT")
    address = models.CharField(max_length=225, verbose_name="Dirección Fiscal")
    city = models.CharField(max_length=225, verbose_name="Ciudad")
    phone = models.CharField(max_length=255, verbose_name="Telefono(s)")
    email = models.CharField(max_length=255, verbose_name="Correo")
    services = models.TextField(verbose_name="Servicios")
    logo = models.ImageField(upload_to='img/logo', null=True, blank=True)
    logoInvoice = models.ImageField(upload_to='img/logo', null=True, blank=True)

    def __str__(self):
        return '{}.{}'.format(self.name, self.nit)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['logo'] = str(self.logo)
        item['logoInvoice'] = str(self.logoInvoice)
        return item
    
    class Meta:
        verbose_name = "Información de la Empresa"
        ordering = ['id']

class Eventos(models.Model):
    name = models.CharField(max_length=255, verbose_name='Evento')
    description = models.CharField(max_length=255, verbose_name='Descripción')
    day = models.DateField(max_length=50, default=date.today().strftime('%Y-%m-%d'), verbose_name='Fecha')
    color = models.CharField(max_length=250, default='#007bff', verbose_name='Color')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Eventos'
        verbose_name_plural = 'Eventos'
        ordering = ['id']

# NEW MODELS

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Categoría', unique=True)
    description = models.TextField(verbose_name="Descripción")
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']

# Model for Competitor
class Team(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre y Apellido')
    dni = models.CharField(max_length=150, verbose_name='Cédula de Identidad')
    birthdate = models.DateField(max_length=50, default=date.today().strftime('%Y-%m-%d'), verbose_name='Fecha de Nacimiento')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Masculino', verbose_name="Género")
    email = models.EmailField(max_length=150, verbose_name='Correo')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Categoría")
    logo = models.ImageField(upload_to='img/team', null=True, blank=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return '{} ({})'.format(self.name, self.category.name)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['category'] = self.category.toJSON()
        item['logo'] = str(self.logo)
        return item
    
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['id']

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.PROTECT, verbose_name="Equipo")
    name = models.CharField(max_length=150, verbose_name='Nombre del Jugador')
    status = models.IntegerField(default=1)

    def __str__(self):
        return '{}.{}'.format(self.name)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['team'] = self.team.toJSON()
        return item
    
    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        ordering = ['id']

class Tournament(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre del Torneo")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Categoría")
    datejoined = models.DateField(max_length=10, default=date.today().strftime('%Y-%m-%d'), verbose_name="Fecha")
    qtyLosses = models.IntegerField(default=0, verbose_name="Número de Pérdidas")
    status = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return '{} ({})'.format(self.name, self.category.name)

    def toJSON(self):
        item = model_to_dict(self)
        item['category'] = self.category.toJSON()
        item['det'] = [i.toJSON() for i in self.dettournament_set.all()]
        return item
    
    class Meta:
        verbose_name = 'Torneo'
        verbose_name_plural = 'Torneos'
        ordering = ['id']

class DetTournament(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    plays = models.IntegerField(default=0)
    earned = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    tied = models.IntegerField(default=0)
    removed = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    lastOpponent = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE, related_name="lastOpponent")

    def __str__(self):
        return self.tournament.name
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['tournament'])
        item['team'] = self.team.toJSON()
        if self.lastOpponent is not None:
            item['lastOpponent'] = self.lastOpponent.toJSON()
        return item

    class Meta:
        verbose_name = 'Detalle de Torneo'
        verbose_name_plural = 'Detalle de Torneos'
        ordering = ['id']

class Confrontations(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT)
    team1 = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="Team1")
    team2 = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="Team2")
    roundNumber = models.IntegerField(default=0)
    qtyRound1 = models.IntegerField(default=0)
    qtyRound2 = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.tournament.name
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['tournament'])
        item['team1'] = self.team1.toJSON()
        item['team2'] = self.team2.toJSON()
        item['det'] = [i.toJSON() for i in self.detconfrontations_set.all()]
        return item

    class Meta:
        verbose_name = 'Enfrentamiento'
        verbose_name_plural = 'Enfrentamientos'
        ordering = ['id']

class Ridding(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    roundNumber = models.IntegerField(default=0)
    free = models.IntegerField(default=0)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.roundNumber
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['tournament'])
        item['team'] = self.team.toJSON()
        return item

    class Meta:
        verbose_name = 'Equipo Librando'
        verbose_name_plural = 'Equipos Librando'
        ordering = ['id']

class DetConfrontations(models.Model):
    confrontation = models.ForeignKey(Confrontations, on_delete=models.PROTECT)
    winner = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="WinningTeam")
    loser = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="LosingTeam")

    def __str__(self):
        return self.confrontation.name
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['confrontation'])
        item['winner'] = self.winner.toJSON()
        item['loser'] = self.loser.toJSON()
        return item

    class Meta:
        verbose_name = 'Detalle de Enfrentamiento'
        verbose_name_plural = 'Detalle de Enfrentamientos'
        ordering = ['id']
