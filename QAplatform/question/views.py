from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from question.models import Question
import json

# Create your views here.
def home(request):
    question = Question.objects.all()
    return render(request,'home.html',{'question':question})

def search(request):
    res = request.POST.get('question')
    con = Question.objects.filter(questionDescription__icontains=res)
    data = []
    for question in con:
        data.append({
            'title':question.questionTitle,
            'time':question.createTime,
            'status':question.status,
            'type':question.get_questionType_display,
            'description':question.questionDescription
        })
    print(data)
    return render(request,'home.html',{'data':data})

def subQuestion(request):
    return render(request,'subQuestion.html')