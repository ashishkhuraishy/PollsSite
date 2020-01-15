from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    result = get_list_or_404(Question.objects.get(pk=question_id).choice_set.all())
    return render(request, 'polls/details.html', {"choice_list":result})

def results(request, question_id):
    response = "You're looking at result of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
