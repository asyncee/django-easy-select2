from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import CreateView
from easy_select2 import select2_modelform

from .models import Note


class NoteCreateView(CreateView):
    model = Note
    form_class = select2_modelform(Note)
    success_url = reverse_lazy('note-list')


class NoteEditView(UpdateView):
    model = Note
    form_class = select2_modelform(Note)
    success_url = reverse_lazy('note-list')


class NoteListView(ListView):
    model = Note
