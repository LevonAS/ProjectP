from django.shortcuts import render

from mainapp.models import QuestionAnswer

def index(request):
    # print('///  question_answer : ', QuestionAnswer.objects.all())
    # for item in QuestionAnswer.objects.filter(main=True):
    #     print(item.question, item.answer)
    context = {'question_answer': QuestionAnswer.objects.filter(main=True)}

    return render(request, 'mainapp/index.html', context)
