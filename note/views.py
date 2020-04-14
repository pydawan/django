from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import NoteForm
from .models import Note


class NoteIndex(ListView):
    template_name = 'note/index.html'
    context_object_name = 'notes'
    queryset = Note.objects.all().order_by('-updated_at')


class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note/create.html'
    success_url = reverse_lazy("note:index")


class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note/create.html'
    success_url = reverse_lazy("note:index")


class NoteDelete(DeleteView):
    model = Note
    template_name = 'base/snippets/confirm-delete.html'
    success_url = reverse_lazy("note:index")
