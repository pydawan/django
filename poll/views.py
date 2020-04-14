from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Choice, Question


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(published=True).order_by('-updated_at')[:5]


class DetailView(DetailView):
    model = Question
    template_name = 'poll/detail.html'


class ResultsView(DetailView):
    model = Question
    template_name = 'poll/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': 'Nenhuma opção foi selecionada.',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Sempre retornar `HttpResponseRedirect` quando uma operação
        # de post tiver sucesso.
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))
