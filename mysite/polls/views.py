import datetime
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import generic

from .models import Answer, Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


def get_queryset(self):
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

@csrf_exempt
def get_question(request):
    if request.method == 'POST':
        question = request.POST
        question_text = list(question.items())[0][1]
        form = Question(question_text = question_text, pub_date = datetime.datetime.now())
        form.save()
    else:
        form = Question()
    return render(request, 'polls/new_question.html', {'form': form})

@csrf_exempt
def get_comment(request, pk):
    if request.method == 'POST':
        comment = request.POST
        comment_text = list(comment.items())[0][1]
        form = Answer(answer_text = comment_text, question_id = pk)
        form.save()
    else:
        form = Answer()
    return render(request, 'polls/new_comment.html', {'form': form})
