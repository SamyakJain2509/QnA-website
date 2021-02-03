from django.shortcuts import render, HttpResponseRedirect, reverse 
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

def index(request):
    return render(request, 'qna/index.html')

@login_required
def question_list(request):
    questions = Question.objects.all()

    return render(request, 'qna/questions.html',{
        'questions':questions,
    })

@login_required
def ask(request):
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.asker = request.user 
            new_question.save()
            return HttpResponseRedirect(reverse('questions'))

    return render(request, 'qna/ask.html',{
        'form':form
    })

@login_required
def question_detail(request, pk):
    question = Question.objects.get(pk=pk)

    form = AnswerForm()
    
    if request.method == 'POST':
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.author = request.user 
            new_answer.question = question
            new_answer.save()
            return HttpResponseRedirect(reverse('questions'))

    return render(request, 'qna/detail.html',{
        'question':question,
        'form':form
    })
