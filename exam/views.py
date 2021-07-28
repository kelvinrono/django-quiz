from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
 
# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuestionModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for question in questions:
            total+=1
            print(request.POST.get(question.question))
            print(question.ans)
            print()
            if question.ans ==  request.POST.get(question.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=QuestionModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'Quiz/home.html',context)
 
def addQuestion(request):    
    if request.user.is_staff:
        form=AddQuestionform()
        if(request.method=='POST'):
            form=AddQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'Quiz/addQuestion.html',context)
    else: 
        return redirect('home') 