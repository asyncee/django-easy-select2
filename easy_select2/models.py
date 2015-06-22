# coding: utf-8

#
# Models `Related`, `TestFieldsModel` and `EmptyModel` are
# used only in tests.
#


from django.db import models


class Related(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False


class TestFieldsModel(models.Model):
    CHOICES = ((0, 'Zero'), (1, 'One'))
    choice_field = models.IntegerField(choices=CHOICES)
    fk_field = models.ForeignKey(Related, related_name='+')
    m2m_field = models.ManyToManyField(Related, related_name='+')
    text = models.TextField()

    class Meta:
        managed = False


class EmptyModel(models.Model):

    class Meta:
        managed = False
