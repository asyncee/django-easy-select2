from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name


class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)  # To demonstrate select2
    categories = models.ManyToManyField(Category)  # To demonstrate select2 multiple

    def __unicode__(self):
        return u'Note %d' % self.id
