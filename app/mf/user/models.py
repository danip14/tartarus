from django.contrib.auth.models import AbstractUser
from config.settings import MEDIA_URL, STATIC_URL
from django.db import models
from django.forms import model_to_dict

class User(AbstractUser):
    image = models.ImageField(upload_to='Users/', null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions','last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        item['full_name'] = self.get_full_name()
        item['image'] = self.get_image()
        return item
