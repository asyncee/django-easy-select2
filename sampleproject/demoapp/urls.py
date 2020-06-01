from django.urls import path

from .views import NoteCreateView, NoteEditView, NoteListView

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('create', NoteCreateView.as_view(), name='note-create'),
    path('<pk>/edit', NoteEditView.as_view(), name='note-edit'),
]
