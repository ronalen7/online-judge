from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

from .models import Problem

# Create your views here.


def Index(request):
    problem_list = Problem.objects.all()
    context = {
        'problem_list': problem_list
    }
    return render(request, 'onlineJudge/index.html', context)


def Detail(request, problem_id):
    return HttpResponse("this is problem no. %s" % problem_id)
