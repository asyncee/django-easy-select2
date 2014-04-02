from django.db import models
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class MarkupType(models.Model):
    text = models.CharField(max_length=50)

    def __unicode__(self):
        return self.text


class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)  # To demonstrate select2
    tags = models.ManyToManyField(Tag)  # To demonstrate select2 multiple
    # To demonstrate select2 text input
    # This field stores id of a MarkupType. We can't use ForeignKey because of
    # django choices validation (see admin.py)
    markup = models.PositiveIntegerField(blank=True, db_index=True)
