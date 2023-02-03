from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    this_url = '/polls/{}/detail.html'
    this_url.format(question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Aint no damn question here')
    return render(request, this_url, {'question': question})


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
