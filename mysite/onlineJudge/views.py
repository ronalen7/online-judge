from multiprocessing import context
from pickle import FALSE, TRUE
from django.utils import timezone
from urllib import request
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core.files import File
import os
import subprocess
import filecmp

from .models import Problem, Solution, Testcase

# Create your views here.


def Index(request):
    problem_list = Problem.objects.all()
    context = {
        'problem_list': problem_list
    }
    return render(request, 'onlineJudge/index.html', context)


def Detail(request, problem_id):
    try:
        problem = Problem.objects.get(pk=problem_id)
        sampleTestcase = Testcase.objects.filter(problem=problem_id)
    except:
        raise Http404("Problem Does Not Exist")
    return render(request, 'onlineJudge/detail.html', {'problem': problem, 'sampleTestcase': sampleTestcase})


def submitProblem(request, problem_id):
    f = request.FILES['solution']
    with open('E:/Placement_Material/project5-Online_Judge/mysite/onlineJudge/input_output_solution_files/solution.cpp', 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)

    sampleTestcase = Testcase.objects.filter(problem=problem_id)
    # for i in sampleTestcase:
    #     print(i.input)
    #     print(i.output)

    # verdict = ''
    verdict = True
    for case in sampleTestcase:
        # fetching given input from Testcase table and storing it in input.txt
        # iFile = open('C:/Users/ASUS/outputFiles/input.txt', 'w')
        iFile = open(
            'E:/Placement_Material/project5-Online_Judge/mysite/onlineJudge/input_output_solution_files/input.txt', 'w')
        iFile.write(case.input)
        # print(iFile)
        iFile.close

        # printing data of input.txt in terminal
        # iFile = open('C:/Users/ASUS/outputFiles/input.txt', 'r')
        iFile = open(
            'E:/Placement_Material/project5-Online_Judge/mysite/onlineJudge/input_output_solution_files/input.txt', 'r')
        data = iFile.read()
        print("input -> " + data)
        iFile.close

        # fetching actual output from Testcase table and storing it in ActualOutput.txt
        # oFile = open('C:/Users/ASUS/outputFiles/ActualOutput.txt', 'w')
        oFile = open(
            'E:/Placement_Material/project5-Online_Judge/mysite/onlineJudge/input_output_solution_files/ActualOutput.txt', 'w')
        oFile.write(case.output)
        # print(oFile)
        oFile.close

        # printing data of ActualOutput.txt in terminal
        # oFile = open('C:/Users/ASUS/outputFiles/ActualOutput.txt', 'r')
        oFile = open(
            'E:/Placement_Material/project5-Online_Judge/mysite/onlineJudge/input_output_solution_files/ActualOutput.txt', 'r')
        data = oFile.read()
        print("output -> " + data)
        oFile.close

        # compiling and executing the user submitted solution
        # subprocess.call(
        #     "g++ C:/Users/ASUS/outputFiles/solution.cpp", shell=True)
        # subprocess.call(
        #     "a.exe <C:/Users/ASUS/outputFiles/input.txt> C:/Users/ASUS/outputFiles/output.txt", shell=True)
        subprocess.call(
            "g++ E:/Placement_Material/project5-Online_Judge/mysite/onlineJudge/input_output_solution_files/solution.cpp", shell=True)
        subprocess.call(
            "a.exe <E:/Placement_Material/project5-Online_Judge/mysite/onlineJudge/input_output_solution_files/input.txt> E:/Placement_Material/project5-Online_Judge/mysite/onlineJudge/input_output_solution_files/output.txt", shell=True)

        userOutput = 'E:/Placement_Material/project5-Online_Judge/mysite/onlineJudge/input_output_solution_files/output.txt'
        actualOutput = 'E:/Placement_Material/project5-Online_Judge/mysite/onlineJudge/input_output_solution_files/ActualOutput.txt'

        # printing data of output.txt in terminal
        oFile = open(
            'E:/Placement_Material/project5-Online_Judge/mysite/onlineJudge/input_output_solution_files/output.txt', 'r')
        data = oFile.read()
        print("user output -> " + data)
        oFile.close

        if(filecmp.cmp(userOutput, actualOutput, shallow=False)):
            # verdict = verdict + "Accepted "
            verdict = verdict and True
        else:
            # verdict = verdict + "Wrong Answer "
            verdict = verdict and False

    print(verdict)

    solution = Solution()
    solution.problem = Problem.objects.get(pk=problem_id)
    solution.verdict = "Accepted" if verdict else "Wrong Answer"
    solution.submitted_at = timezone.now()
    solution.submitted_code = 'E:/Placement_Material/project5-Online_Judge/mysite/onlineJudge/input_output_solution_files/solution.cpp'
    solution.save()

    if(verdict == True):
        return render(request, 'onlineJudge/verdict.html', {'verdict': verdict})
    else:
        return render(request, 'onlineJudge/verdict.html', {'verdict': verdict})
