from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # To demonstrate select2
    categories = models.ManyToManyField(Category)  # To demonstrate select2 multiple

    def __unicode__(self):
        return u'Note %d' % self.id

    def __str__(self):
        return 'Note %d' % self.id


class Related(models.Model):
    name = models.CharField(max_length=50)


class TestFieldsModel(models.Model):
    CHOICES = ((0, 'Zero'), (1, 'One'))
    choice_field = models.IntegerField(choices=CHOICES)
    fk_field = models.ForeignKey(Related, related_name='+', on_delete=models.CASCADE)
    m2m_field = models.ManyToManyField(Related, related_name='+')
    text = models.TextField()


class EmptyModel(models.Model):
    pass
