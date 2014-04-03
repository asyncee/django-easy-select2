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
    # To demonstrate select2 text input
    mood = models.CharField(blank=False, default='', max_length=64,
                            help_text='What is your current mood?')

    def __unicode__(self):
        return u'Note %d' % self.id
